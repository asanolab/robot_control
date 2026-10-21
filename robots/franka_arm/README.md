# panda

## robot model
![panda_rviz_wide](https://github.com/asanolab/robot_control/assets/6872136/aaadd6e9-3a1e-4244-8c4f-17610334c5e8)

![panda_pedestal_rviz_wide](https://github.com/asanolab/robot_control/assets/6872136/19f10748-4d8c-4dda-ba2f-b43f4bf42e8f)

---

# Franka Research 3 (FR3) セットアップ

> 対象: Ubuntu 20.04.6 LTS / ROS Noetic / FR3 System Image 5.3.0  
> 状態: セットアップ手順案（実機での動作検証は未実施）  
> 注: このフォルダには従来の Panda 関連ファイルもあるため、既存の Panda 用設定を FR3 用と混同しないこと。

## 1. バージョンと準備

- Ubuntu: 20.04.6 LTS
- ROS: Noetic (ROS 1)
- FR3 System Image: 5.3.0
- libfranka: **0.10.0** を候補として固定
- franka_ros: **0.10.0** を候補として固定（FR3 対応を含むリリース）
- FCI (Franka Control Interface) が利用可能であること

**重要:** System Image と libfranka / franka_ros の互換性は必ず公式の互換性表とリリースノートで再確認すること。ROS Noetic はサポート終了済みのため、研究用PCではバージョンを固定して利用する。実機を動かす前に安全領域、非常停止、ブレーキ解除状態を確認する。

参考:
- [libfranka](https://github.com/frankarobotics/libfranka)
- [franka_ros](https://github.com/frankarobotics/franka_ros)
- [Franka Robotics Documentation](https://frankarobotics.github.io/docs/)

## 2. Setup workspace
```bash
sudo apt install python3-vcstool

cd catkin_ws
vcs import src < src/catkin_ws/src/robot_control/franka_arm/repositories/franka_arm.repos
rosdep install -y -r --from-paths src --ignore-src
  # pr2_teleop_general in jsk_pr2_startup is obsolete
```

## 2. libfranka をビルド

```bash
cd libfranka
git checkout 0.10.0
git submodule update --init --recursive
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF ..
cmake --build . -j$(nproc)
```

## 3. ros build

```bash
cd src/robot_control/franka_arm
catkin bt
source ~/catkin_ws/devel/setup.bash
```

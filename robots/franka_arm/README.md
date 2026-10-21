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

## 2. PC と FR3 のネットワーク

PC と FR3 Control の FCI 用 Ethernet ポートを有線接続する。以下のアドレスは**例**であり、実際の Control 側の設定を先に確認する。

| 機器 | IP アドレス例 |
| --- | --- |
| Ubuntu PC | `172.16.0.1/24` |
| FR3 Control | `172.16.0.2/24` |

インターフェース名と通信確認:

```bash
ip -br addr
ping -c 4 172.16.0.2
```

Franka Desk のアクセス先（例）: `https://172.16.0.2`。アクセスできない場合、LAN 接続・PC と Control の IP 設定・FCI の有効化を確認する。

## 3. ROS / ビルドツール

ROS Noetic がインストール済みであることを確認する。

```bash
source /opt/ros/noetic/setup.bash
rosversion -d
sudo apt update
sudo apt install -y build-essential cmake git libpoco-dev libeigen3-dev python3-rosdep
```

`rosversion -d` が `noetic` を返すこと。

## 4. libfranka をビルド

**既存の libfranka がある場合は、混在させずバージョン・インストール先を確認する。**

```bash
mkdir -p ~/franka_setup
cd ~/franka_setup
git clone --recursive https://github.com/frankarobotics/libfranka.git
cd libfranka
git checkout 0.10.0
git submodule update --init --recursive
mkdir -p build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF ..
cmake --build . -j$(nproc)
```

CMake の依存関係やオプションは指定したタグの README を優先する。問題が発生した場合は CMake のエラー全文を記録する。

## 5. franka_ros / Catkin ワークスペース

```bash
mkdir -p ~/franka_setup/catkin_ws/src
cd ~/franka_setup/catkin_ws/src
git clone --recursive https://github.com/frankarobotics/franka_ros.git
cd franka_ros
git checkout 0.10.0
git submodule update --init --recursive

cd ~/franka_setup/catkin_ws
source /opt/ros/noetic/setup.bash
rosdep install --from-paths src --ignore-src --rosdistro noetic --skip-keys libfranka -y
catkin_make -DCMAKE_BUILD_TYPE=Release -DFranka_DIR=$HOME/franka_setup/libfranka/build
source devel/setup.bash
rospack find franka_control
rospack find franka_description
```

`Franka_DIR` が解決できない場合は `find ~/franka_setup/libfranka/build -name 'FrankaConfig.cmake'` で実際の CMake 設定ディレクトリを確認する。既存 Catkin ワークスペースに取り込む場合は重複する `franka_ros` を置かない。

## 6. ロボット状態の取得（最初の実機テスト）

Franka Desk で FCI モードの利用条件を確認後、**ロボットを動かさず**状態取得テストを実施する。コマンドの実行前に緊急停止と周囲の安全を確認する。

```bash
cd ~/franka_setup/libfranka/build
./examples/echo_robot_state 172.16.0.2
```

この実行ファイルがない場合、`find . -name echo_robot_state -type f` で位置と、例プログラムがビルドされているか確認する。

## 7. ROS 動作確認

```bash
source /opt/ros/noetic/setup.bash
source ~/franka_setup/catkin_ws/devel/setup.bash
rospack list | grep franka
```

その後、指定した `franka_ros` タグの launch 引数を確認して **robot=fr3** などの FR3 モデル指定があるか調べる。Panda 向けの起動引数をそのまま FR3 に流用しない。RViz のみの確認から開始し、`franka_control` による実機接続、コントローラ起動、動作指令へと段階的に進める。

## 8. リアルタイム通信と安全

FCI による 1 kHz 制御にはリアルタイム設定が重要。以下で現在のカーネルを確認する。

```bash
uname -a
uname -v
```

必要に応じて、公式ガイドに従い Ubuntu 20.04 用の PREEMPT_RT カーネル、ユーザーのリアルタイム優先度上限、CPU 省電力設定などを確認する。ネットワーク遅延やジッタが大きい環境で、いきなり動作制御を実行しない。

## 9. トラブルシューティング

| 症状 | 確認事項 |
| --- | --- |
| `ping` が失敗 | LAN ポート、ケーブル、IP、サブネット、ファイアウォール |
| Desk に入れない | Desk 用 IP、HTTPS、Control 起動状態 |
| `libfranka` 接続エラー | FCI 有効化、System Image との互換性、ネットワーク |
| ビルド失敗 | タグ、サブモジュール、Poco/Eigen/CMake、他バージョンとの競合 |
| ROS がパッケージを見つけない | `source devel/setup.bash`、`ROS_PACKAGE_PATH` |
| リアルタイム関連エラー | PREEMPT_RT、ユーザー権限、通信ジッタ |
| モデルが Panda になる | FR3 用ロボットモデル・launch 引数を確認 |

## 10. 動作確認チェックリスト

- [ ] Ubuntu 20.04.6 LTS / ROS Noetic を確認
- [ ] FR3 System Image 5.3.0 を確認
- [ ] 公式互換性表と採用タグを確認
- [ ] PC と Control の IP 設定を記録
- [ ] Franka Desk にアクセス
- [ ] FCI 利用条件を確認
- [ ] libfranka をビルド
- [ ] franka_ros をビルド
- [ ] 状態取得テストに成功
- [ ] FR3 モデルを RViz で確認
- [ ] リアルタイム設定・安全確認を完了
- [ ] 実機の動作テストを別途承認・実施

## 作業ログ

| 日付 | PC / カーネル | System Image | libfranka | franka_ros | 確認者 / 備考 |
| --- | --- | --- | --- | --- | --- |
| 2026-10-21 | Ubuntu 20.04.6 / 未確認 | 5.3.0 | 0.10.0（候補） | 0.10.0（候補） | 手順書追加・実機未検証 |

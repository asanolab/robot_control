# nextage_nxa_interface
## Memo
- NEXTAGE(NXA)は、産業版（研究開発用のオープン版ではない）。カワダ製ソフトウェアによる制御。
- APIによって自前開発のソフトウェアとの連携が可能。
  - APIはカワダより取得する。
- 外部PCとの通信は、corba通信。そのためomniORBとomniORBpyが必要。
  - python3が推奨(3.8, 3.10). omniORBpyのbuildが必要になる
  - pytyon2だと、ユニコード問題や今後の環境構築の制約になりうるので.
  - NEXTAGE PC(Windows)でFirewallの設定が必要。

- 動作確認
  - ubuntu20.04
  - python3.8
  - omniORB-4.2.4
  - omniORBpy-4.2.4

## Setup
### Install & Build
- Install
```
sudo apt install libomniorb4-dev omniorb-idl omniidl build-essential
```

- python3
  - build
    1. buildスクリプトを実行する. 
    ```
    cd install
    sudo ./build.sh
    ```
    2. sourceforgeから,直接omniORB-4.2.4とomniORBpy-4.2.4をダウンロードしてbuildしてもよい.
      - https://sourceforge.net/projects/omniorb/files/omniORB
      - https://sourceforge.net/projects/omniorb/files/omniORBpy
  - pathを.bashrcに追加
  ```
  export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.8/site-packages  # for omniORBpy
  export PYTHONPATH=$PYTHONPATH:/PATH_to_API/NxApiSdk/python/lib
  export PYTHONPATH=$PYTHONPATH:/PATH_to_API/NxApiSdk/python/lib/NxApiLib/idl_NxApi
  ```

- python2
  - omniorbはaptでインストール出来る
  ```
  sudo apt install python-omniorb
  ```

### NEXTAGE PC(windows)の設定
- Firewallの設定
  - 「コントロールパネル」から「Windowsファイアウォール」->「Windows ファイアウォールを介したアプリまたは機能を許可」
  - 「NxProduction ...」の行の「プライベートネットワーク」の行のチェックボックスをONにする。
  - 再起動



## 実装上のメモ
### バージョンによる注意点
- python3.8の場合  
anyは、omniORBからimport (API manualに記載)
  ```
  from omniORB import CORBA, any as ANY
  ```

- python3.10の場合  
anyは、NxApiLibからimportする. (配布されているサンプルプログラム参照. python3.8と3.10で何か変わった？)
  ```
  from omniORB import CORBA
  from NxApiLib import any as ANY
  ```

- python2の場合  
anyはomniORBからimportする
  ```
  from omniORB import CORBA, any as ANY
  ```
  また,文字列をユニコードと指定するために、
  ```
  "test" -> u"text"
  とする。
  ```

## 本体操作
- 復帰方法
  - 肩LEDが黄色 -> 「Release Pose」をクリック -> 肩LEDが緑になる
  - 

## トラブルシューティング
- NEXTAGEと通信できない
  ```
  root_controller = api._narrow(RootNxController)
  File "/usr/local/lib/python3.8/site-packages/omniORB/CORBA.py", line 583, in _narrow
  return self._obj.narrow(repoId, 1)
  omniORB.CORBA.TRANSIENT: CORBA.TRANSIENT(omniORB.TRANSIENT_ConnectFailed, CORBA.COMPLETED_NO)
  ```
  - ファイアウォール設定を確認

- controller.Execute(u"GetAuthority", ANY.to_any(None)) で止まる
  ```
  return self._obj.invoke("Execute", _0_NxApi.NxObject._d_Execute, args)
  omniORB.CORBA.NO_PERMISSION: CORBA.NO_PERMISSION(0x0, CORBA.COMPLETED_YES)
  ```
  - APIサーバが外部通信モードか確認. External control mode deactivated (黄緑)だとNG. クリックして, External control mode activated (黄色) に変更

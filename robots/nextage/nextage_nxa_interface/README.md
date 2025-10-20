# nextage_nxa_interface

# Setup
## Memo
- python3が推奨(3.8, 3.10). omniORBpyのbuildが必要になる
- pytyon2だと、ユニコード問題や今後の環境構築の制約になりうるので.

- 動作確認
  - ubuntu20.04
  - python3.8
  - omniORBpy4.2.4

## Build
corba通信のためにomniORBとomniORBpyが必要  

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
  export PYTHONPATH=/usr/local/lib/python3.8/site-packages:$PYTHONPATH
  ```


- python2
  - omniorbはaptでインストール出来る
  ```
  sudo apt install python-omniorb
  ```

## バージョンによる注意点
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
  ```
  とする。

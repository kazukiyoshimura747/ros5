# 課題２
ロボットシステム学の課題として入力された整数を半径とする円の面積と円周の長さを出力するプログラムを作成した。

pub_radius.pyでは任意の整数を入力し半径とする。
sub_area.pyでは入力された整数を受け取り、面積を計算し出力する。
単位は(cm*2)とする。
sub_circumference.pyでは入力された整数を受け取り、円周の長さを計算し出力する。単位は(cm)とする

# 動作環境
* OS  Ubuntu Server 20.04.2.3LTS

* ROS noetic

* ハードウェア Raspberry Pi 3 ModelB

# 実行
端末1でROSを立ち上げる。
```
roscore
```
端末2でpub_radius.pyを実行する。
```
rosrun ros5 pub_radiis.py
```
端末3でsub_area.pyを実行する。
```
rosrun ros5 sub_area.py
```
端末4でsub_circumference.pyを実行する。
```
rosrun ros5 sub_circumference.py
```
# 実行結果
下記のリンクよりこのパッケージの動作が確認できる。


<https://youtu.be/6n_8_xnLCC8>

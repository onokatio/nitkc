後期 実験2 割り込みによるデータ入出力実験
===

# 1. 目的
H8マイコンの A/D, D/A変換器とPWM制御について理解を深め,それらを用いて
音声録音再生プログラムを作成する。
# 2. 方法

本章では , H8 マイコンに内蔵 されて いるAD変換器, D/A変換器を用いて音声録音再生プログラムを作成する 。それらの詳細は各節を参照 すること , ad_init() と da_init()を用いて初期化し,使用準備を整える。録音モードの時にA/D 変換により音声データをディジタル信号へ変換 し, 記憶領域databuf[] へ格納する.また, 再生モードの時にD/A変換にて databud ] 内のデータをアナログ信号へ変換 し, スピーカから 再生している .なお, ADSTATUS() と ADREADCは関数 の形に見えているが,実際は ad.h で定義さ れて いるマクロである.実験準備として,「/home/class/53/jikken/kouki/no2』以下にあるファイルを各自コピーするその上で, 以下の課題についてプログラムを作成 し動作確認を 行う.

## 2.1 音の記録·再生

サンブルプログラム(rec.c)内のコメント 文の指示に従ってプログラムを完成さ せよ。スピーカ兼マイクは ,録音モード時にマイク として機能し,再生モード時には スピーカとして機能 する。「* 」キーを押すと録音 モードとなり, マイクから音を入力 すると音響信号データが保存される」「#」キーを押すと再生モードとなり、スピーカから音が再生される。
なお, 再生音の音高が録音し た音と一致 するか否かは問わないこととする.

## 2.2 音の記録·再生と, LED の光量の連動

音量の大小 に応じて, LED の先量を明由化させるプログラムを作成せよ、ただし, 光量変化の 職密性は問わないことと する.

## 2.3シンクロスコープによる波形観測
PWMの出力波形をシンクロスコープ で観測する。 デューティ比は, 21院と50とする 。 シンクロスコープのBUN/STOPキーを用いてもよいが 、安定した周期信号を 出力するように無限ループさせることを推奨する。

# 3. 結果

## 3-1
ad_startし、ADSTATUSが完了するまで待機することで録音をした。また、pwm_databufをループの中でPWM制御出力することで、再生ができるようになった。
## 3-2
3-1のコードを使い、音量を制御するPWMの波がオンの範囲になった場合のみ、LEDを点灯させた。

## 3-3
音量制御部分を、256のうち51以上の場合のみ出力することで、PWMのデューティ比を20%に固定した。また、比較記号を逆転することで、80%に固定することもできた。
以下4に、シンクロスコープの結果をしめす。

# 4. 観察した波形
画像3.1 シンクロスコープ20%
![](https://i.imgur.com/Q7QVbpZ.jpg)

画像3.2 シンクロスコープ80%

![](https://i.imgur.com/wQE2Syx.jpg)

# 5. 検討課題
## 5-1 サンプリング周期の大小がデータに与える影響について
サンプリング周期が短いほど、データの時間のこまかさが荒くなるため、制度は下がると考えられる。
## 5-2 PWM制御がアナログ的な電圧変化に比べて有利な点
アナログ回路なしのデジタル回路のみでも、電圧の大小を表現することができる。

# 6. 感想

自分の書いたコードで、声を録音できるのがびっくりした。楽しかった。
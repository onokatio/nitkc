実験3 H8マイコンを用いたスイッチ入力実験
===

# 1. 目的
H8マイコンのスイッチ入力の基本的な扱い方を理解する。

# 2. 使用機器
- H8ワンボードマイコン 
- パーソナルコンピュータ

# 3. 実験方法

まず, `/home/class/j3/jikkan/zanki/no3` 以下にある次の2つのサンプルプログラムをコピーする.

- key-sample.c
- make-key

以下の設問についてプログラムを作成し, 動作確認を行う。なお, スタッフに動作確認をしてもらい確認印をもらうこと.

## 3.1 スイッチ入力によるLED点灯
 「1」スイッチを入力し,その後スイッチを離した後も赤色LEDは点灯し続ける。「0」スイッチを入力すると赤色LEDは消灯し,同様にスイッチを離した後も赤色LEDは点灯し続けること.

## 3.2 スイッチ入力した1文字のLCD表示
いずれかのスイッチを入力し,その入力したスイッチに対応する文字を表示させるプログラムを作成せよ、表示させる文字は0~9までの数字と,「* 」と「#」の計12種類とする.なお,入力後にスイッチを離しても、他のキーを押すまで同じ文字を表示し続けるものとする。

## 3.3 スイッチ入力した文字列のLCD表示

スイッチを入力し,その入力した文字列を表示させるプログラムを作成せよ.表示させる文字は 0~9までの数字と,「* 」と「#」の計12種類とする。

このとき,すでに入力した文字はそのまま表示を保持し 、新しく入力 した 文字を その右隣に表示するチャタリング対策をして,スイッチを押したままでも,対応する文字を1つ表示する.すなわち,スイッチを押している間に同じ文字が連続して並ぶということがないようにする

また, 1行目の右端にたどりついたら2行目の左端から続けて表示する2行目の右端までたどりついた後の処理 は問わないこととする.

チャタリング対策のための待ち時間処理は,キー入力があったときのみ働くようにすることとし,常に待ち時間処理を行わないようにする.また, チャタリング対策は,キーを押したときと、離した ときの両方で行うこと

なお, キー入力処理を関数化することは少し難しいが、挑戦してみることも 面白い.

# 4. 実験結果

## 4-1 スイッチ入力によるLED点灯
PADRとP6DRを用いて、ダイナミック入力を行った。
結果、キー入力を検知できた。

ソースコードをリスト3.1に示す。

リスト1.3
```c
#include "h8-3052-iodef.h"

int main(void)
{
  unsigned char cf, key_data;

  P9DDR = 0x30;  /* ポート9の初期化(P95-P94を出力に設定) */

  P6DDR &= ~0x07;  /* P60,1,2   入力 */
  PADDR |= 0x0f;   /* PA0,1,2,3 出力 */

  P9DR = 0x30;  /* D1(赤)消灯, D2(緑)消灯 */

  while(1) {
    key_data = 0;

    //key 1,2,3
    PADR = 0x07; // PA3 = L
    cf = P6DR;   // データ入力
    cf = ~cf;    // cfの反転
    cf &= 0x07;  // P60,1,2のみ見る
    switch(cf) {
    case 1 : key_data = '1'; break;
    case 2 : key_data = '2'; break;
    case 4 : key_data = '3'; break;
    }  
      
    //key 4,5,6
    PADR = 0x0b;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '4'; break;
    case 2 : key_data = '5'; break;
    case 4 : key_data = '6'; break;
    }  
      
    //key 7,8,9
    PADR = 0x0b; /* This is a mistake code. */
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '7'; break;
    case 2 : key_data = '8'; break;
    case 4 : key_data = '9'; break;
    }  
      
    //key *,0,#
    PADR = 0x0e;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '*'; break;
    case 2 : key_data = '0'; break;
    case 4 : key_data = '#'; break;
    }  
    
    if(key_data == '1' ) {
      P9DR = 0x20;  /* D1(赤)点灯, D2(緑)消灯 */
    }
    if(key_data == '0' ) {
      P9DR = 0x30;  /* D1(赤)消灯, D2(緑)消灯 */
    }

  }

}
```

## 4-2 スイッチ入力した1文字のLCD表示
4-1と同じようにダイナミック入力を使用した。また、過去のキーを覚えておくことで他のキーを押すまで入力を保持することができた。

ソースコードをリスト3.2に示す。

リスト3.2
```c
#include "h8-3052-iodef.h"
#include "lcd.h"

int main(void)
{
  unsigned char cf, key_data;

  P9DDR = 0x30;  /* ポート9の初期化(P95-P94を出力に設定) */

  P6DDR &= ~0x07;  /* P60,1,2   入力 */
  PADDR |= 0x0f;   /* PA0,1,2,3 出力 */

  P9DR = 0x30;  /* D1(赤)消灯, D2(緑)消灯 */

	lcd_init();

  key_data = ' ';
  while(1) {

    //key 1,2,3
    PADR = 0x07; // PA3 = L
    cf = P6DR;   // データ入力
    cf = ~cf;    // cfの反転
    cf &= 0x07;  // P60,1,2のみ見る
    switch(cf) {
    case 1 : key_data = '1'; break;
    case 2 : key_data = '2'; break;
    case 4 : key_data = '3'; break;
    }  
      
    //key 4,5,6
    PADR = 0x0b;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '4'; break;
    case 2 : key_data = '5'; break;
    case 4 : key_data = '6'; break;
    }  
      
    //key 7,8,9
    PADR = 0x0d; /* This is a mistake code. */
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '7'; break;
    case 2 : key_data = '8'; break;
    case 4 : key_data = '9'; break;
    }  
      
    //key *,0,#
    PADR = 0x0e;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '*'; break;
    case 2 : key_data = '0'; break;
    case 4 : key_data = '#'; break;
    }  
    
		lcd_cursor(0,0);
		lcd_printch(key_data);

  }

}
```

## 4-3 スイッチ入力した文字列のLCD表示
ダイナミック入力を使用した。また、チャタリング除去のため、重みをつけ、一定時間の間キー入力を検知した場合のみ入力判定とした。

ソースコードをリスト3.3に示す。

リスト3.3

```c
#include "h8-3052-iodef.h"
#include "lcd.h"
#include "stdio.h"

int main(void)
{
  unsigned char cf, key_data, key_data_old;
	char str[32] = {};
	int i = 0;
	int j = 0;
	int weight[12] = {};
	int pushed[12] = {};
	int keycode = 12;
	//int temp;

  P9DDR = 0x30;  /* ポート9の初期化(P95-P94を出力に設定) */

  P6DDR &= ~0x07;  /* P60,1,2   入力 */
  PADDR |= 0x0f;   /* PA0,1,2,3 出力 */

  P9DR = 0x30;  /* D1(赤)消灯, D2(緑)消灯 */

	lcd_init();

  while(1) {

		key_data_old = key_data;
		key_data = 0;

    //key 1,2,3
    PADR = 0x07; // PA3 = L
    cf = P6DR;   // データ入力
    cf = ~cf;    // cfの反転
    cf &= 0x07;  // P60,1,2のみ見る
    switch(cf) {
    case 1 : key_data = '1'; break;
    case 2 : key_data = '2'; break;
    case 4 : key_data = '3'; break;
		}  
      
    //key 4,5,6
    PADR = 0x0b;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '4'; break;
    case 2 : key_data = '5'; break;
    case 4 : key_data = '6'; break;
    }  
      
    //key 7,8,9
    PADR = 0x0d;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '7'; break;
    case 2 : key_data = '8'; break;
    case 4 : key_data = '9'; break;
    }  
      
    //key *,0,#
    PADR = 0x0e;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : key_data = '*'; break;
    case 2 : key_data = '0'; break;
    case 4 : key_data = '#'; break;
    }  
    
		if(key_data - '0' >= 0 && key_data - '0' <= 9){
			keycode = key_data - '0';
		}else if(key_data == '*'){
			keycode = 10;
		}else if(key_data == '#'){
			keycode = 11;
		}else{
			keycode = 12;
		}

		if(key_data == key_data_old){
			weight[keycode]++;
		}

		for(i = 0; i < 12 ; i++){
			if(pushed[i] == 0 && weight[i] > 100){
				for(j = 0; j < 12; j++){
					pushed[j] = 0;
					weight[j] = 0;
				}
				pushed[i] = 1;
				weight[i] = 0;
				if(i == 10){
					lcd_printch('*');
				}else if(i == 11){
					lcd_printch('*');
				}else{
					lcd_printch('0' + i);
				}
			}
		}

  }

}

```
# 5. 検討課題

## 5-1. チャタリングに対する有効な方法
ソフトウェア制御の場合、リングバッファ方式と、待ち時間方式がある。ハードウェア制御の場合、バタフライ回路の方法がある。

## 5-2. ダイナミックスキャン入力の長所と短所
長所はIOポート数が少ない点である。短所はソフトウェアの実装が複雑になる点である。
## 5-3. キーボード回路のダイオードの役割
ダイナミックスキャンをする際に、使用していないポートに電流が流れるのを阻止する役割がある。

実験実習 実験1 タイマ割り込み実験
===

# 1. 目的
H8マイコンの割り込みについて理解を深め、割り込み制御をC言語で記述する方法を学ぶ。

# 2. 使用機器

使用機器の表を、表1.1に示す。

| 機器名 | メーカー名 | 型番 | シリアルナンバー |
| :---: | :------: | :-: | :-----------: |
| H8マイコン|Byond the river|20060904|29|

表1.1 使用機器

# 3. 実験方法

## 3.1 課題1 LED 点滅実験

1秒間隔で赤色LED (D1)と緑色LED (D2)を交互に点滅させるプログラムを作成せよ、ただし、タイマ0を使用して 1ms ごとに割り込みをかけるものとし、割り込みハンドラでは呼び出されるたびに、大域変数 sys_time を0から1ずつ増やし、その値の 1000 ごとに大域変数 sec_time を0から1ずつ増やすこと。つまり、 sec_timeが1秒毎に1ずつ増加することになる。それ以外の機能は、全てメインルーチン内で実装すること。なお、 タイマ0 による割り込みハンドラの関数は void int_imiao(void)とすること。また、雛形にはこれらが全て含まれた構造が与えられているので参考にすること。

## 3.2 課題2 時計表示実験

前期の実験2を参考に、 LCD に時間を表示するプログラムを作成せよ。タイマ割り込み関連は、今回の実験の課題1で作成したものを利用してよい。

### 課題 2-1

プログラム実行からの秒数を表示するプログラムを作成せよ。ただし、秒数が変化したときだけ表示を更新するものとする。なお、 LCD の持つ桁数まで対応させてもよいし、 int 型の表現できる上限までを扱うということでもよい。

### 課題 2-2

プログラム実行時から経過した時分秒を表示するプログラムを作成せよ。時計表示の範囲は、 00:00:00 から 23:59:59 とし、 23:59:59 の次は 00:00:00 に戻り、計時を続ける。なお、 プログラムの動作確認のために 23:59:55 から計時を開始すること。

### 課題2-3

$\frac{1}{100}$ 秒まで表示できるようにして、ストップウォッチの機能を実現せよ。0キーでリセットされて00:00:00.00 を表示するとともに、計時ストップとする。また、 * キーで計時スタート、 #キーで計時ストップとする。なお、 23:59:59.99 までを表示し、 00:00:00.00 には戻らないものとする。 

### 課題2-4

課題2-2 で作成した時計に、 キー入力によって時刻を合わせる機能を付加せよ。時刻合わせの方法は各自に任せるが、少なくとも時と分の単位で任意の時刻に設定できるようにすること。また、 時刻セット時は、 キー入力したらすぐに画面に反映させることとし、後で一度に表示するのは不可とする。

# 4. 実験結果

## 課題1

課題1のソースファイルを以下に示す。

リスト1.1 blink.c
```c=
#include "h8-3052-iodef.h"
#include "h8-3052-int.h"
#include "timer.h"

/* 割り込みの周期 1000us */
#define INT1MS 1000

/* 割り込み処理に必要な変数は大域変数にとる \*/
/* volatile はプログラムの流れとは無関係に変化する変数に必ずつける */
volatile unsigned int sys_time;
volatile unsigned int sec_time; /* 1秒毎に +1 される変数を確保 */

/* 割り込みハンドラのプロトタイプ宣言 */
void int_imia0(void);

int main(void)
{
  ROMEMU(); /* ROMエミュレーションをON (割り込み使用時必須) */

  /* 時間を格納する変数の初期化 */
  sys_time = 0;
  sec_time = 0;

  /* LEDの接続されているポートの初期化をここに書く (実験1参照) */
	P9DDR = 0x30; 


  timer_init();        /* タイマを使用前に初期化する */
  timer_set(0,INT1MS); /* タイマ0を1ms間隔で動作設定 */
  timer_start(0);      /* タイマ(チャネル0)スタート  */

  ENINT();             /* CPU割り込み許可 */

  while (1) {
    /* 割り込み動作以外はこの無限ループを実行している */

    /* ここに sec_time の値によってLEDを光らせるプログラムを書く */
    /*   1秒ごとに 赤→緑→赤→緑→… と交互に点滅させる         */
	if (sec_time % 2 == 0){
		P9DR = 0x20;
	}else{
		P9DR = 0x10;
	}


  }
  return 1; /* mainからの戻り値はエラーレベルを表す 0:正常終了 */
            /* 永久ループの外なので,戻ったら何かおかしい       */
}

#pragma interrupt
void int_imia0(void)
     /*
      *  タイマ0の割り込みハンドラ
      *    タイマ0 から割り込み要求がくると，この関数が呼び出される．
      *  タイマ0 の割り込みの場合は，この関数の名前（int_imia0）と
      *  決まっている．
      *    関数の直前に割り込みハンドラ指定の #pragma interrupt が必要．
      */
{
  /* 割り込みハンドラの処理が軽くなるように配慮すること \*/
  /* 外でできる処理はここには書かない \*/

  /* sys_time の更新 ( +1 する) をここに書く */
	sys_time++;

  
  /* ここに sec_time の更新 ( +1 する) を書く */
	if (sys_time % 1000 == 0){
		sec_time++;
	}
  
  /* 再びタイマ割り込みを使用するために必要な操作      \*/
  /*   タイマ0の割り込みフラグをクリアしないといけない */
  timer_intflag_reset(0);

  ENINT();       /* CPUを割り込み許可状態に */
}
```

このプログラムでは、現在の秒数が奇数か偶数か判断する。前者の場合緑、後者の場合赤色のLEDを点灯させる。

## 課題2-1

課題2-1のソースファイルを以下に示す。

リスト1.2 time.c

```c=
#include "h8-3052-iodef.h"
#include "h8-3052-int.h"
#include "timer.h"
#include "lcd.h"

/* 割り込みの周期 1000us */
#define INT1MS 1000

/* 割り込み処理に必要な変数は大域変数にとる \*/
/* volatile はプログラムの流れとは無関係に変化する変数に必ずつける */
volatile unsigned int sys_time;
volatile unsigned int sec_time; /* 1秒毎に +1 される変数を確保 */
volatile unsigned int old_time;

/* 割り込みハンドラのプロトタイプ宣言 */
void int_imia0(void);

int main(void)
{
  ROMEMU(); /* ROMエミュレーションをON (割り込み使用時必須) */
  lcd_init();

  /* 時間を格納する変数の初期化 */
  sys_time = 0;
  sec_time = 0;
  old_time = 0;

  timer_init();        /* タイマを使用前に初期化する */
  timer_set(0,INT1MS); /* タイマ0を1ms間隔で動作設定 */
  timer_start(0);      /* タイマ(チャネル0)スタート  */

  ENINT();             /* CPU割り込み許可 */

  while (1) {
    /* 割り込み動作以外はこの無限ループを実行している */

	if (old_time != sec_time){
	// 時間が更新されている場合、現在の時間を表示する。
  		lcd_cursor(0,0);
		printnum(sec_time);
		old_time = sec_time;
	}

  }
  return 1; /* mainからの戻り値はエラーレベルを表す 0:正常終了 */
            /* 永久ループの外なので,戻ったら何かおかしい       */
}

void printnum(unsigned int num){ // 再帰で数値を文字列として出力する関数。
	if (num != 0){
		printnum(num/10);
	}else{
		return;
	}

	lcd_printch((num % 10) + '0');
}

#pragma interrupt
void int_imia0(void)
     /*
      *  タイマ0の割り込みハンドラ
      *    タイマ0 から割り込み要求がくると，この関数が呼び出される．
      *  タイマ0 の割り込みの場合は，この関数の名前（int_imia0）と
      *  決まっている．
      *    関数の直前に割り込みハンドラ指定の #pragma interrupt が必要．
      */
{
  /* 割り込みハンドラの処理が軽くなるように配慮すること \*/
  /* 外でできる処理はここには書かない \*/

  /* sys_time の更新 ( +1 する) をここに書く */
	sys_time++;

  
  /* ここに sec_time の更新 ( +1 する) を書く */
	if (sys_time % 1000 == 0){
		sec_time++;
	}
  
  /* 再びタイマ割り込みを使用するために必要な操作      \*/
  /*   タイマ0の割り込みフラグをクリアしないといけない */
  timer_intflag_reset(0);

  ENINT();       /* CPUを割り込み許可状態に */
}

```

このプログラムは、無限ループの中で、時間をカウントする変数が更新されている場合、つまり1秒経過している場合のみ、時刻をLCDに表示する。

## 課題2-2

課題2-2のソースファイルを以下に示す。

リスト1.3 spent.c

```c=
#include "h8-3052-iodef.h"
#include "h8-3052-int.h"
#include "timer.h"
#include "lcd.h"

/* 割り込みの周期 1000us */
#define INT1MS 1000

/* 割り込み処理に必要な変数は大域変数にとる \*/
/* volatile はプログラムの流れとは無関係に変化する変数に必ずつける */
volatile unsigned int sys_time;
volatile unsigned int sec_time; /* 1秒毎に +1 される変数を確保 */
volatile unsigned int old_time;

/* 割り込みハンドラのプロトタイプ宣言 */
void int_imia0(void);

int main(void)
{
  ROMEMU(); /* ROMエミュレーションをON (割り込み使用時必須) */
  lcd_init();

  /* 時間を格納する変数の初期化 */
  sys_time = 0;
  sec_time = 0;
  old_time = 0;

  int h = 23;
  int m = 59;
  int s = 55;

  timer_init();        /* タイマを使用前に初期化する */
  timer_set(0,INT1MS); /* タイマ0を1ms間隔で動作設定 */
  timer_start(0);      /* タイマ(チャネル0)スタート  */

  ENINT();             /* CPU割り込み許可 */

	lcd_cursor(0,0); // 初期状態を表示する。
	lcd_printch(h / 10 + '0');
	lcd_printch(h % 10 + '0');
	lcd_printch(':');
	lcd_printch(m / 10 + '0');
	lcd_printch(m % 10 + '0');
	lcd_printch(':');
	lcd_printch(s / 10 + '0');
	lcd_printch(s % 10 + '0');

  while (1) {
    /* 割り込み動作以外はこの無限ループを実行している */

	if (old_time != sec_time){
	//時刻が更新されている場合のみ、時刻表示を更新する。
		s++;
		if(s > 59) m += 1; //以下、繰上がりの制御をしている。
			s %= 60;
		if(m > 59) h += 1;
			m %= 60;
		if(h > 23) h = 0;

  		lcd_cursor(0,0); //時刻を表示している。
		lcd_printch(h / 10 + '0');
		lcd_printch(h % 10 + '0');
		lcd_printch(':');
		lcd_printch(m / 10 + '0');
		lcd_printch(m % 10 + '0');
		lcd_printch(':');
		lcd_printch(s / 10 + '0');
		lcd_printch(s % 10 + '0');
		old_time = sec_time;
	}

  }
  return 1; /* mainからの戻り値はエラーレベルを表す 0:正常終了 */
            /* 永久ループの外なので,戻ったら何かおかしい       */
}

void printnum(unsigned int num){
	if (num != 0){
		printnum(num/10);
	}else{
		return;
	}

	lcd_printch((num % 10) + '0');
}

#pragma interrupt
void int_imia0(void)
     /*
      *  タイマ0の割り込みハンドラ
      *    タイマ0 から割り込み要求がくると，この関数が呼び出される．
      *  タイマ0 の割り込みの場合は，この関数の名前（int_imia0）と
      *  決まっている．
      *    関数の直前に割り込みハンドラ指定の #pragma interrupt が必要．
      */
{
  /* 割り込みハンドラの処理が軽くなるように配慮すること \*/
  /* 外でできる処理はここには書かない \*/

  /* sys_time の更新 ( +1 する) をここに書く */
	sys_time++;

  
  /* ここに sec_time の更新 ( +1 する) を書く */
	if (sys_time % 1000 == 0){
		sec_time++;
	}
  
  /* 再びタイマ割り込みを使用するために必要な操作      \*/
  /*   タイマ0の割り込みフラグをクリアしないといけない */
  timer_intflag_reset(0);

  ENINT();       /* CPUを割り込み許可状態に */
}

```

このプログラムでは、時刻が更新されている場合のみ、起動してからの時刻を時分秒の形式に直して表示する。

## 課題2-3

課題2-3のソースファイルを以下に示す。

リスト1.4 stopwatch.c

```c=
#include "h8-3052-iodef.h"
#include "h8-3052-int.h"
#include "timer.h"
#include "lcd.h"

/* 割り込みの周期 1000us */
#define INT1MS 1000

/* 割り込み処理に必要な変数は大域変数にとる \*/
/* volatile はプログラムの流れとは無関係に変化する変数に必ずつける */
volatile unsigned int sys_time;
volatile unsigned int sec_time; /* 1秒毎に +1 される変数を確保 */
volatile unsigned int secD100_time; /* 0.1秒毎に +1 される変数を確保 */
volatile unsigned int oldD100_time;

/* 割り込みハンドラのプロトタイプ宣言 */
void int_imia0(void);

int main(void)
{
  ROMEMU(); /* ROMエミュレーションをON (割り込み使用時必須) */
  lcd_init();

  /* 時間を格納する変数の初期化 */
  sys_time = 0;
  sec_time = 0;
  secD100_time = 0;
  oldD100_time = 0;

  int h = 23;
  int m = 59;
  int s = 55;
  int sD100 = 0;

  int run = 0;

  unsigned char cf, key_data, key_data_old;
	int i = 0;
	int j = 0;
	int weight[12] = {};
	int pushed[12] = {};
	int keycode = 12;

  P9DDR = 0x30;  /* ポート9の初期化(P95-P94を出力に設定) */

  P6DDR &= ~0x07;  /* P60,1,2   入力 */
  PADDR |= 0x0f;   /* PA0,1,2,3 出力 */

  timer_init();        /* タイマを使用前に初期化する */
  timer_set(0,INT1MS); /* タイマ0を1ms間隔で動作設定 */
  timer_start(0);      /* タイマ(チャネル0)スタート  */

  ENINT();             /* CPU割り込み許可 */

  		lcd_cursor(0,0);
		lcd_printch(h / 10 + '0');
		lcd_printch(h % 10 + '0');
		lcd_printch(':');
		lcd_printch(m / 10 + '0');
		lcd_printch(m % 10 + '0');
		lcd_printch(':');
		lcd_printch(s / 10 + '0');
		lcd_printch(s % 10 + '0');
		lcd_printch('.');
		lcd_printch(sD100 / 10 + '0');
		lcd_printch(sD100 % 10 + '0');

  while (1) {
    /* 割り込み動作以外はこの無限ループを実行している */

		key_data_old = key_data;
		key_data = 0;

    PADR = 0x0e;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : keycode = 10; break;
    case 2 : keycode = 0; break;
    case 4 : keycode = 11; break;
    }
		if(key_data == key_data_old){
			weight[keycode]++;
		}

		for(i = 0; i < 12 ; i++){ //ダイナミック入力
			if(pushed[i] == 0 && weight[i] > 100){
				for(j = 0; j < 12; j++){
					pushed[j] = 0;
					weight[j] = 0;
				}
				pushed[i] = 1;
				weight[i] = 0;
				if(i == 10){
					run = 1;
				}else if(i == 11){
					run = 0;
				}else if(i == 0){
					run = 0;
					sD100 = 0;
					s = 0;
					m = 0;
					h = 0;
					lcd_cursor(0,0);
					lcd_printch(h / 10 + '0');
					lcd_printch(h % 10 + '0');
					lcd_printch(':');
					lcd_printch(m / 10 + '0');
					lcd_printch(m % 10 + '0');
					lcd_printch(':');
					lcd_printch(s / 10 + '0');
					lcd_printch(s % 10 + '0');
					lcd_printch('.');
					lcd_printch(sD100 / 10 + '0');
					lcd_printch(sD100 % 10 + '0');
				}
			}
		}

	if (run == 1 && oldD100_time != secD100_time){
	// 100分の一秒の変数を作り、更新を検出している。
		sD100++;
		if(sD100 > 99) s += 1;
			sD100 %= 100;
		if(s > 59) m += 1;
			s %= 60;
		if(m > 59) h += 1;
			m %= 60;
		if(h > 23){
			run = 0;
			h = 23;
			m = 59;
			s = 59;
			sD100 = 99;
		}

  		lcd_cursor(0,0);
		lcd_printch(h / 10 + '0');
		lcd_printch(h % 10 + '0');
		lcd_printch(':');
		lcd_printch(m / 10 + '0');
		lcd_printch(m % 10 + '0');
		lcd_printch(':');
		lcd_printch(s / 10 + '0');
		lcd_printch(s % 10 + '0');
		lcd_printch('.');
		lcd_printch(sD100 / 10 + '0');
		lcd_printch(sD100 % 10 + '0');
		oldD100_time = secD100_time;
	}

  }
  return 1; /* mainからの戻り値はエラーレベルを表す 0:正常終了 */
            /* 永久ループの外なので,戻ったら何かおかしい       */
}

void printnum(unsigned int num){
	if (num != 0){
		printnum(num/10);
	}else{
		return;
	}

	lcd_printch((num % 10) + '0');
}

#pragma interrupt
void int_imia0(void)
     /*
      *  タイマ0の割り込みハンドラ
      *    タイマ0 から割り込み要求がくると，この関数が呼び出される．
      *  タイマ0 の割り込みの場合は，この関数の名前（int_imia0）と
      *  決まっている．
      *    関数の直前に割り込みハンドラ指定の #pragma interrupt が必要．
      */
{
  /* 割り込みハンドラの処理が軽くなるように配慮すること \*/
  /* 外でできる処理はここには書かない \*/

  /* sys_time の更新 ( +1 する) をここに書く */
	sys_time++;

  
  /* ここに sec_time の更新 ( +1 する) を書く */
	if (sys_time % 1000 == 0){
		sec_time++;
	}
	if (sys_time % 10 == 0){
		secD100_time++;
	}
  
  /* 再びタイマ割り込みを使用するために必要な操作      \*/
  /*   タイマ0の割り込みフラグをクリアしないといけない */
  timer_intflag_reset(0);

  ENINT();       /* CPUを割り込み許可状態に */
}

```

このプログラムでは、前記の実験3で実装した、ダイナミック入力を用いている。
指示通りのキーを押すと、それに従い、時間が停止、再開、リセットされる。
100分の1秒を実現するため、そのための変数も用意した。

## 課題2-4

課題2-4のソースファイルを以下に示す。

リスト1.5 watch.c

```c=
#include "h8-3052-iodef.h"
#include "h8-3052-int.h"
#include "timer.h"
#include "lcd.h"

/* 割り込みの周期 1000us */
#define INT1MS 1000

/* 割り込み処理に必要な変数は大域変数にとる \*/
/* volatile はプログラムの流れとは無関係に変化する変数に必ずつける */
volatile unsigned int sys_time;
volatile unsigned int sec_time; /* 1秒毎に +1 される変数を確保 */
volatile unsigned int old_time;

/* 割り込みハンドラのプロトタイプ宣言 */
void int_imia0(void);

int main(void)
{
  ROMEMU(); /* ROMエミュレーションをON (割り込み使用時必須) */
  lcd_init();

  /* 時間を格納する変数の初期化 */
  sys_time = 0;
  sec_time = 0;
  old_time = 0;

  int force_print = 0;

  int h = 0;
  int m = 0;
  int s = 0;
  int sD100 = 0;

  unsigned char cf;
	int i = 0;
	int j = 0;
	int weight[12] = {};
	int pushed[12] = {};
	int keycode = 12;
	int keycode_old = 12;

  P9DDR = 0x30;  /* ポート9の初期化(P95-P94を出力に設定) */

  P6DDR &= ~0x07;  /* P60,1,2   入力 */
  PADDR |= 0x0f;   /* PA0,1,2,3 出力 */

  timer_init();        /* タイマを使用前に初期化する */
  timer_set(0,INT1MS); /* タイマ0を1ms間隔で動作設定 */
  timer_start(0);      /* タイマ(チャネル0)スタート  */

  ENINT();             /* CPU割り込み許可 */

  		lcd_cursor(0,0);
		lcd_printch(h / 10 + '0');
		lcd_printch(h % 10 + '0');
		lcd_printch(':');
		lcd_printch(m / 10 + '0');
		lcd_printch(m % 10 + '0');
		lcd_printch(':');
		lcd_printch(s / 10 + '0');
		lcd_printch(s % 10 + '0');

  while (1) {
    /* 割り込み動作以外はこの無限ループを実行している */

		keycode_old = keycode;
		keycode = 0;

    PADR = 0x07; // PA3 = L
    cf = P6DR;   // データ入力
    cf = ~cf;    // cfの反転
    cf &= 0x07;  // P60,1,2のみ見る
    switch(cf) {
    case 1 : keycode = 1; break;
    case 2 : keycode = 2; break;
    case 4 : keycode = 3; break;
	}  
      
    //key 4,5,6
    PADR = 0x0b;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : keycode = 4; break;
    case 2 : keycode = 5; break;
    case 4 : keycode = 6; break;
    }  
      
    //key 7,8,9
    PADR = 0x0d;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : keycode = 7; break;
    case 2 : keycode = 8; break;
    case 4 : keycode = 9; break;
    }  
    PADR = 0x0e;
    cf = P6DR;
    cf = ~cf;
    cf &= 0x07;
    switch(cf) {
    case 1 : keycode = 10; break;
    case 2 : keycode = 0; break;
    case 4 : keycode = 11; break;
    }
	if(keycode == keycode_old){
		weight[keycode]++;
		//lcd_cursor(0,1);
		//printnum(weight[1]);
	}else{
		for(j = 0; j < 12; j++){
			pushed[j] = 0;
			weight[j] = 0;
		}
	}

	for(i = 0; i < 12 ; i++){
		if(pushed[i] == 0 && weight[i] > 500){
			for(j = 0; j < 12; j++){
				pushed[j] = 0;
				weight[j] = 0;
			}
			pushed[i] = 1;
			weight[i] = 0;
			//入力キーを判別し、時分秒の変数を増加、減少させている。
			if(i == 1 && h < 24) h++;
			if(i == 4 && h > 0) h--;
			if(i == 2 && m < 60) m++;
			if(i == 5 && m > 0) m--;
			if(i == 3 && s < 60) s++;
			if(i == 6 && s > 0) s--;
			force_print = 1;
		}else if(pushed[i] == 1 && weight[i] > 500){
			weight[i] = 0;
			pushed[i] = 0;
		}
	}

	if (old_time != sec_time){
		s++;
		if(s > 59) m += 1;
			s %= 60;
		if(m > 59) h += 1;
			m %= 60;
		if(h > 23) h = 0;

  		lcd_cursor(0,0);
		lcd_printch(h / 10 + '0');
		lcd_printch(h % 10 + '0');
		lcd_printch(':');
		lcd_printch(m / 10 + '0');
		lcd_printch(m % 10 + '0');
		lcd_printch(':');
		lcd_printch(s / 10 + '0');
		lcd_printch(s % 10 + '0');
		old_time = sec_time;
	}
	if (force_print){
		force_print = 0;
  		lcd_cursor(0,0);
		lcd_printch(h / 10 + '0');
		lcd_printch(h % 10 + '0');
		lcd_printch(':');
		lcd_printch(m / 10 + '0');
		lcd_printch(m % 10 + '0');
		lcd_printch(':');
		lcd_printch(s / 10 + '0');
		lcd_printch(s % 10 + '0');
	}

  }
  return 1; /* mainからの戻り値はエラーレベルを表す 0:正常終了 */
            /* 永久ループの外なので,戻ったら何かおかしい       */
}

void printnum(unsigned int num){
	if (num != 0){
		printnum(num/10);
	}else{
		return;
	}

	lcd_printch((num % 10) + '0');
}

#pragma interrupt
void int_imia0(void)
     /*
      *  タイマ0の割り込みハンドラ
      *    タイマ0 から割り込み要求がくると，この関数が呼び出される．
      *  タイマ0 の割り込みの場合は，この関数の名前（int_imia0）と
      *  決まっている．
      *    関数の直前に割り込みハンドラ指定の #pragma interrupt が必要．
      */
{
  /* 割り込みハンドラの処理が軽くなるように配慮すること \*/
  /* 外でできる処理はここには書かない \*/

  /* sys_time の更新 ( +1 する) をここに書く */
	sys_time++;

  
  /* ここに sec_time の更新 ( +1 する) を書く */
	if (sys_time % 1000 == 0){
		sec_time++;
	}
  
  /* 再びタイマ割り込みを使用するために必要な操作      \*/
  /*   タイマ0の割り込みフラグをクリアしないといけない */
  timer_intflag_reset(0);

  ENINT();       /* CPUを割り込み許可状態に */
}

```

このプログラムでは、1と4、2と5、3と6のキーで、それぞれ時、分、秒の変数の内容を変更できるようになっている。また、本来は1秒更新であるが、キー入力されたときのみ強制的に画面の更新をしている。

# 5. 検討課題

## 検討課題1

sys_timeの型は unsigned int である。32ビット表現の場合、この最大値は 4,294,967,295 となる。単位は$\frac{1}{1000}$秒である。

24時間は60 * 60 * 24秒で86400秒、つまり1000分の1秒の世界で86400 * 1000の大きさとなる。 上の数字をこの数字で割ると、**49あまり61367295**になる。
60分は、1000 * 60 * 60で、3600000 の大きさになる。
61367295 を3600000で割ると **17あまり167295**になる。
167295 を 1000 * 60で割ると、 **2あまり47295**となる。

よって、時分秒に直すと、 1193時間（49日*24+17時間）と2分と47.295秒になる。

## 検討課題2

割り込みハンドラは、関数が呼ぶのではなく、CPU外部や内部の割り込みによって実行されるものであるため、呼び出す側が引数を指定することはできない、また意味がない。
もちろん、呼び出し元は関数呼出しをしていないため、返り値を返すこともできない。

もし呼び出し元が値を渡したり、割り込みハンドラの中で値を返したい場合、メモリマップドIOや、メモリの特定の領域、スタックなどを使うのが良い。
マインスイーパー
==


# 仕様

## 外部仕様

0. 実行ファイルを実行することで、アプリケーションを起動できる。
1. アプリケーションを開始すると、9✕9のマスが用意される。
2. ユーザーは、`input (x y)`というプロンプトに対して、半角空白区切りで開けたいマスの座標を入力できる。

## 内部仕様


内部では、地雷があるかどうかの情報と周りの地雷の数を保管する二次元配列(ms)、またマスが開いているかどうかを保管する二次元配列(isOpen)の計2つの配列を保持している。
前者は、二次元配列を使い、地雷がある場所に-1を保管することで地雷の状態を保管している。
以下、簡略化のために前者をms、後者isOpenと表記する。

main関数では各機能ごとの関数を呼び出すことに注力している。


以下にmain関数から呼び出される関数の定義を日本語で表す。

また、各関数はグローバル変数などを用いていないため、ユーザーに入力を指せる関数と、乱数を生成する関数を除きすべて副作用が取り除かれている。

以下manコマンドと同じ構造でのマニュアルである。

```
SYNOPSIS

	void init(int ms[sizeX][sizeY]);
	void setRandom(int ms[sizeX][sizeY]);
	void dump(int ms[sizeX][sizeY]);
	void setNumber(int ms[sizeX][sizeY]);
	int getHereNum(int inputX,int inputY, int ms[sizeX][sizeY]);
	void start(int ms[sizeX][sizeY],int isOpen[sizeX][sizeY]);

DESCRIPTION

	init
		msの状態とランダム関数のシードが初期化される。
	
	setRandom
		msが、指定した数の地雷をランダムに配置された状態になる。

	setNumber
		周りの地雷の数を計測し、nsが地雷のないマスへ保管された状態になる。

	getHereNum
		inputX,inputYで指定された座標の、左右上下8マスにいくつ地雷があるか数え、値を返す。

	prompt
		ユーザーの入力(inputX,inputY)を受け取り、変数に保管する。

	show
		msとisOpenの状態から、今のマインスイーパーの盤面の状態を画面に描画する。

	calcFail
		座標で指定されたマスを開く。開いた結果、地雷があったか、なかったか、もしくはすでに開いていたかの3種類のうちのどれかを結果として返す。

	calcAutoOpen
		隣接したマスを自動で開く。内容が思いつかなかったため特に意味はなく何もしていない。

	start
		ゲームオーバーになるまで、ユーザーの入力を受け取り、処理をし、描画をする関数。ゲームを続ける。

	dump
		デバッグ用の関数。msの内容をすべて画面に表示する。

```

# プログラムの正しさ

- ゲームオーバー時には、画面に文字が表示される。
	- 実際にゲームオーバーを試し、== Game Over. ==と表示されることを確認した。
- 想定外の文字を入力した場合（数値が異様に大きいなど）は安全のために強制終了するようにしている。
  - 検証方法として、文字の'a'を入力し、終了することを確認した。

# 問題点

- 自動でマスを開ける機能がない。
- ユーザーがマスの数と地雷の数を指定できない。
- エンターキーをわざわざ幼いと座標を決定できない。

# プログラムリスト

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define sizeX 10
#define sizeY 10
#define mineNum 10

void init(int ms[sizeX][sizeY]);
void setRandom(int ms[sizeX][sizeY]);
void dump(int ms[sizeX][sizeY]);
void setNumber(int ms[sizeX][sizeY]);
int getHereNum(int inputX,int inputY, int ms[sizeX][sizeY]);
void start(int ms[sizeX][sizeY],int isOpen[sizeX][sizeY]);

int main(void){

        int ms[sizeX][sizeY];
        int isOpen[sizeX][sizeY];

        init(ms);
        init(isOpen);

        setRandom(ms);

        //dump(ms);

        setNumber(ms);

        //dump(ms);

        printf("\n");

        start(ms,isOpen);

        return 0;

}
void init(int ms[sizeX][sizeY]){
        int i;
        int j;
        srand((unsigned)time(NULL));

        for(i=0;i<sizeX;i++){
                for(j=0;j<sizeY;j++){
                        ms[i][j] = 0;
                }
        }
}

void setRandom(int ms[sizeX][sizeY]){
        int randX;
        int randY;
        int i;
        i = 0;
        while(i<mineNum){
                randX = rand()%sizeX;
                randY = rand()%sizeY;
                if( ms[randX][randY] == 0){
                        ms[randX][randY] = -1;
                        i++;
                }
        }
}

void dump(int ms[sizeX][sizeY]){
        int i;
        int j;
        for(j=0;j<sizeY;j++){
                for(i=0;i<sizeX;i++){
                        printf("%d ",ms[i][j]);
                }
                printf("\n");
        }
}

void setNumber(int ms[sizeX][sizeY]){
        int i;
        int j;
        for(i=0;i<sizeX;i++){
                for(j=0;j<sizeY;j++){
                        if(ms[i][j] != -1){ ms[i][j] = getHereNum(i,j,ms); };
                }
        }
}

int getHereNum(int inputX,int inputY, int ms[sizeX][sizeY]){
        int count = 0;

        if(inputX != 0)         if(ms[inputX-1][inputY]   == -1) count++;
        if(inputX != sizeX - 1) if(ms[inputX+1][inputY]  == -1) count++;
        if(inputY != 0)         if(ms[inputX][inputY-1]    == -1) count++;
        if(inputY != sizeY - 1) if(ms[inputX][inputY+1] == -1) count++;

        if(inputX != 0         && inputY != 0)         if(ms[inputX-1][inputY-1]     == -1) count++;
        if(inputX != sizeY - 1 && inputY != 0)         if(ms[inputX+1][inputY-1]    == -1) count++;
        if(inputX != 0         && inputY != sizeY - 1) if(ms[inputX-1][inputY-1]     == -1) count++;
        if(inputX != sizeY - 1 && inputY != sizeY - 1) if(ms[inputX+1][inputY+1] == -1) count++;

        return count;
}

void prompt(int *x,int *y){
        printf("input (x y) ");
        scanf("%d %d",x,y);
}

void show(int ms[sizeX][sizeY],int isOpen[sizeX][sizeY]){
        int i;
        int j;
        printf("    ");
        for(i=0;i<sizeX;i++){
                printf("%d ",i);
        }
        printf("\n");
        printf("   ┌");
        for(i=0;i<sizeX;i++){
                printf("──",i);
        }
        printf("┐\n");
        for(j=0;j<sizeY;j++){
                printf("%d  │",j);
                for(i=0;i<sizeX;i++){
                        if(isOpen[i][j] == 1){
                                if(ms[i][j] == -1){
                                        printf("M");
                                }else if(ms[i][j] == 0){
                                        printf(" ");
                                }else{
                                        printf("%d",ms[i][j]);
                                }
                        }else{
                                printf("■");
                        }
                        printf(" ");
                }
                printf("│\n");
        }
        printf("   └");
        for(i=0;i<sizeX;i++){
                printf("──",i);
        }
        printf("┘\n");
}

int calcFail(int inputX, int inputY, int ms[sizeX][sizeY],int isOpen[sizeX][sizeY]){
        if(isOpen[inputX][inputY] == 1) return 2;

        if(ms[inputX][inputY] == -1){
                return 1;
        }

        return 0;
}

int calcAutoOpen(int inputX, int inputY, int ms[sizeX][sizeY],int isOpen[sizeX][sizeY]){
        int i;
        int j;

        for(j=0;j<sizeY;j++){
                for(i=0;i<sizeX;i++){
                        if(ms[i][j] == 0){
                        }
                }
        }
        int count = 0;
        if(inputX != 0)         if(ms[inputX-1][inputY]   == -1) count++;
        if(inputX != sizeX - 1) if(ms[inputX+1][inputY]  == -1) count++;
        if(inputY != 0)         if(ms[inputX][inputY-1]    == -1) count++;
        if(inputY != sizeY - 1) if(ms[inputX][inputY+1] == -1) count++;

        if(inputX != 0         && inputY != 0)         if(ms[inputX-1][inputY-1]     == -1) count++;
        if(inputX != sizeY - 1 && inputY != 0)         if(ms[inputX+1][inputY-1]    == -1) count++;
        if(inputX != 0         && inputY != sizeY - 1) if(ms[inputX-1][inputY-1]     == -1) count++;
        if(inputX != sizeY - 1 && inputY != sizeY - 1) if(ms[inputX+1][inputY+1] == -1) count++;
}

void start(int ms[sizeX][sizeY],int isOpen[sizeX][sizeY]){
        int inputX;
        int inputY;
        int loop = 1;
        int failReturn;

        while(loop){
                show(ms,isOpen);

                prompt(&inputX,&inputY);
                if(inputX > sizeX-1 || inputY > sizeY-1){
                        printf("Input Value is invalid.");
                        break;
                }

                failReturn = calcFail(inputX, inputY, ms, isOpen);

                if(failReturn == 1){
                        isOpen[inputX][inputY] = 1;
                        show(ms,isOpen);
                        printf("\n == Game Over. == \n");
                        loop = 0;
                }else if(failReturn == 2){
                        printf("\n == The position is already opened. == \n");
                }else{
                        isOpen[inputX][inputY] = 1;
                        calcAutoOpen(inputX, inputY, ms,isOpen);
                }
        }
}

```
Robots
===


# プログラムの仕様（外部仕様，内部仕様）

## プログラムの機能（外部仕様）

このプログラムは、Unixのゲームであるrobotsを実装したものである。

## プログラムの使い方(外部仕様)


ターミナルで、`./robots`と実行する。

## 主要なデータ構造 (内部仕様)

今回は、ロボットの座標と、座標にいるロボットの数とを、2種類の方法で管理した。

このため、「特定の座標にロボットがいるかどうか知りたい」「このロボットがどこの座標にいるか知りたい」といった情報が両方共ループなしに取得できる。

### Robot_single (構造体)

ロボット一つあたりのx,y座標を整数値として覚えている。

### RobotField (配列)

2次元座標を作り、ゲームの盤面の特定の座標に何台ロボットがいるかどうかを数値として管理する。

### ScrapField (配列)

2次元座標を作り、ゲームの盤面の特定の座標にスクラップがあるかどうかを1/0の真偽値として管理する。

### Robots (構造体)

上記3つ（Robot_singleは台数分）をまとめて管理している。

## 各関数の仕様（引数，戻り値・副作用，処理内容）

```
void Robots_Updatexy(struct Robots *robots, int num, int x, int y)
ロボットの情報を2つの方法で管理しているため、変更操作をここで統一して行っている（オブジェクト指向でいうセッター）
void draw(struct Robots *robots,struct Player *player, int *robotnum)
画面病が処理
void teleport_player(struct Robots *robots, struct Player *player)
プレイヤーのテレポート
void move_player(char key, struct Robots *robots,struct Player *player)
プレイヤーの移動
void update_robots(struct Robots *robots,struct Player *player,int *level, int *score,int *robotnum)
ロボットがプレイヤーを追いかける処理
int calc(char key,struct Robots *robots,struct Player *player,int *level, int *score,int *robotnum)
キー入力の分岐
void init_robots(struct Robots *robots,int *robotnum)
主要データの初期化
void init_player(struct Player *player)
プレイヤーの初期化
void play(int *level, int *score)
ゲーム本体
void init(int array[fieldX][fieldY])
配列の初期化
```

#  プログラムの正しさの検証
・衝突，ゲームオーバの処理が正しく行なわれていることの確認

実際に衝突すると、Game Overと表示され終了することを確認した。

・想定外の文字を入力されても破綻しないことの確認

0〜9と、個人的に追加したhjkluinmを除き、他のキーを入力しても動作は破綻しないことを、実際に入力して確認した。

# 各処理の計算量
m = 盤面の縦の大きさ
n = 横の大きさ
q = ロボットの個数

プレイヤ移動
  処理時間: O(1)
  データ領域: O(1)

ロボット移動
  処理時間: O(q)
  データ領域: O(q)

衝突
  処理時間: O(nm)
  データ領域: O(nm)



# 付録としてプログラムリスト
・適切なコメントを含むこと
・インデントをつけるなど，読みやすさに配慮すること
・2段組フォーマットが望ましい（紙資源を大切にしよう）


```c=
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

extern char getChar(void);

#define fieldX 60
#define fieldY 20
#define ROBOTNUM 40

struct Robot_single{
        int x;
        int y;
};

struct Robots{
        struct Robot_single array[ROBOTNUM];
        int RobotField[fieldX][fieldY];
        int ScrapField[fieldX][fieldY];
};

struct Player{
        int x;
        int y;
};


void Robots_Updatexy(struct Robots *robots, int num, int x, int y){

        robots->RobotField[robots->array[num].x][robots->array[num].y]--;

        robots->array[num].x = x;
        robots->array[num].y = y;

        robots->RobotField[x][y]++;
}

void draw(struct Robots *robots,struct Player *player, int *robotnum){
        int i;
        int j;
        int vram[fieldX][fieldY];


        for(j=0;j<fieldY;j++){
                for(i=0;i<fieldX;i++){
                        vram[i][j] = ' ';
                }
        }

        /*
        for(j=0;j<fieldY;j++){
                for(i=0;i<fieldX;i++){
                        printf("%d", robots->ScrapField[i][j]);
                }
                printf("\n");
        }
                printf("\n");
        for(j=0;j<fieldY;j++){
                for(i=0;i<fieldX;i++){
                        printf("%d", robots->RobotField[i][j]);
                }
                printf("\n");
        }
        */

        for(i=0;i<*robotnum;i++){
                if(! robots->ScrapField[robots->array[i].x][robots->array[i].y]){
                        vram[robots->array[i].x][robots->array[i].y] = '+';
                }else{
                        vram[robots->array[i].x][robots->array[i].y] = '*';
                };
        }

        vram[player->x][player->y] = '@';

        printf("\033[2J");
        printf("\n+");
        for(i=0;i<fieldX;i++){
                printf("-");
        }
        printf("+\n");
        for(j=0;j<fieldY;j++){
                printf("|");
                for(i=0;i<fieldX;i++){
                        printf("%c",vram[i][j]);
                }
                printf("|\n");
        }
        printf("+");
        for(i=0;i<fieldX;i++){
                printf("-");
        }
        printf("+\n");
}

void teleport_player(struct Robots *robots, struct Player *player){
        int randx;
        int randy;
        do {
                randx = rand()%fieldX;
                randy = rand()%fieldY;
                player->x=randx;
                player->y=randy;
        } while (robots->RobotField[randx][randy] != 0);
}

void move_player(char key, struct Robots *robots,struct Player *player){
        switch(key){
                case 'h':
                case '4':
                        if(! robots->RobotField[player->x -1][player->y]) player->x--;
                        break;
                case 'l':
                case '6':
                        if(! robots->RobotField[player->x +1][player->y]) player->x++;
                        break;
                case 'j':
                case '2':
                        if(! robots->RobotField[player->x][player->y +1]) player->y++;
                        break;
                case 'k':
                case '8':
                        if(! robots->RobotField[player->x][player->y -1]) player->y--;
                        break;
                case 'u':
                case '7':
                        if(! robots->RobotField[player->x -1][player->y -1]){
                                player->x--;
                                player->y--;
                        }
                        break;
                case 'i':
                case '9':
                        if(! robots->RobotField[player->x +1][player->y -1]){
                                player->x++;
                                player->y--;
                        }
                        break;
                case 'n':
                case '1':
                        if(! robots->RobotField[player->x -1][player->y +1]){
                                player->x--;
                                player->y++;
                        }
                        break;
                case 'm':
                case '3':
                        if(! robots->RobotField[player->x +1][player->y +1]){
                                player->x++;
                                player->y++;
                        }
                        break;
                case '0':
                        teleport_player(robots,player);
                        break;
        }
        if(player->x > fieldX-1) player->x = fieldX-1;
        if(player->x < 0) player->x = 0;
        if(player->y > fieldY-1) player->y = fieldY-1;
        if(player->y < 0) player->y = 0;
        return;
}

void update_robots(struct Robots *robots,struct Player *player,int *level, int *score,int *robotnum){
        for(int i=0;i<*robotnum;i++){
                if(robots->ScrapField[robots->array[i].x][robots->array[i].y] == 1) continue;
                if(robots->array[i].x != player->x){

                        if(robots->array[i].x < player->x){
                                Robots_Updatexy(robots,i,robots->array[i].x+1,robots->array[i].y);
                        }else{
                                Robots_Updatexy(robots,i,robots->array[i].x-1,robots->array[i].y);
                        }

                }
                if(robots->array[i].y != player->y){

                        if(robots->array[i].y < player->y){
                                Robots_Updatexy(robots,i,robots->array[i].x,robots->array[i].y+1);
                        }else{
                                Robots_Updatexy(robots,i,robots->array[i].x,robots->array[i].y-1);
                        }

                }
                if(robots->array[i].x == player->x && robots->array[i].y == player->y){
                        draw(robots,player,robotnum);
                        printf("Game Over\n");
                        exit(0);
                }
        }
        for(int y=0; y < fieldY ; y++){
                for(int x=0; x < fieldX ; x++){
                        if(robots->RobotField[x][y] >= 2 || ( robots->RobotField[x][y] >= 1 && robots->ScrapField[x][y] == 1) ){
                                *score += robots->RobotField[x][y];
                                robots->ScrapField[x][y] = 1;
                                robots->RobotField[x][y] = 0;
                        }
                }
        }

}

int calc(char key,struct Robots *robots,struct Player *player,int *level, int *score,int *robotnum){
        switch(key){
                case 'h':
                case 'l':
                case 'j':
                case 'k':
                case 'u':
                case 'i':
                case 'n':
                case 'm':
                case '0':
                case '1':
                case '2':
                case '3':
                case '4':
                case '6':
                case '7':
                case '8':
                case '9':
                        move_player(key,robots,player);
                case '5':
                        update_robots(robots,player,level,score,robotnum);
                        break;
                default:
                        break;

        }
        return 0;
}

void init_robots(struct Robots *robots,int *robotnum){
        for(int num=0;num<*robotnum;num++){
                do {
                        robots->array[num].x = rand()%fieldX;
                        robots->array[num].y = rand()%fieldY;
                } while( robots->RobotField[robots->array[num].x][robots->array[num].y] == 1);

                robots->RobotField[robots->array[num].x][robots->array[num].y] = 1;
        }
}

void init_player(struct Player *player){
        player->x = rand()%fieldX;
        player->y = rand()%fieldY;
}

void play(int *level, int *score){
        int exitflag = 0;
        struct Robots robots = {};
        struct Player player = {};
        char key;
        int target = 0;

        int robotnum = *level * 5;
        if(robotnum > 40) robotnum = 40;

        target = *score + *level*5;

        init_robots(&robots,&robotnum);
        init_player(&player);

        draw(&robots,&player,&robotnum);

        while(!exitflag){
                printf("\n(level:%d score:%d):?", *level, *score);
                key = getChar();
                calc(key,&robots,&player,level,score,&robotnum);
                draw(&robots,&player,&robotnum);

                printf("targe = %d\n",target);
                if(*score >= target){
                        *score += *level * 10;
                        break;
                }
        }
}

int main(void){

        srand((unsigned)time(NULL));

        int level = 1;
        int score = 0;

        while(1){
                play(&level,&score);
                level++;
        }
}

```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "def.h"
#include "var.h"

#include "bmpfile.h"

int main(int argc, char *argv[])
{
	imgdata idata;
	double c;
	int x,y;

	unsigned char LUT[255];
	unsigned char histogram[255];
	unsigned average = 0;
	int nm[255][255] = {};

	// 例題プログラム
	// 　BMPファイルをコピーするプログラム
	//
	//	 readBMPfile関数でidata.sourceに画像データが読み込まれる
	//	 writeBMPfile関数でidata.resultsの画像データが書きだされる
	//	 これらの関数は、bmpfile.o に入っています
	//	 3次元配列のインデックスは、[RGBの種類][y座標][x座標]
	//	 BMP形式では、画像の左下が座標の原点
	//	 その他、var.h と def.h を見て下さい
	
	if (argc < 3) printf("使用法：cpbmp コピー元.bmp コピー先.bmp\n");
	else {
		if (readBMPfile(argv[1], &idata) > 0)
			printf("指定コピー元ファイル%sが見つかりません\n",argv[1]);
		else {
			for(int i=0;i<255;i++){
				histogram[i] = 0;
			}
			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
					histogram[idata.source[RED][y][x]]++;
					nm[idata.source[RED][y][x]][idata.source[RED][y][x]]++;
				}
			}
			average = (idata.height*idata.width)/255;
			for(int i=0;i<255;i+=4){
				printf("\n");
				for(int j=0;j<(histogram[i]+histogram[i+1])/8;j++) printf("#");
			}

			for(int i=0;i<255;i++){
				if(nm[i][i] < average){
					for(int j=0;nm[i][i] != average;j++){
						int tmp=0;

						// copy from higher item
						if(average - nm[i][i] > nm[i+j][i+j]){
							tmp = nm[i+j][i+j];
						}else{
							tmp = average - nm[i][i];
						}
						nm[i+j][i+j] -= tmp; // delete from higher item
						nm[i+j][i] = tmp; // write log
						nm[i][i] += tmp; // append value from higher item
					}
				}else if(nm[i][i] > average){
					int overflow =  nm[i][i] - average; // send overflow
					nm[i+1][i+1] += overflow; // send overflow
					nm[i][i] = average; // cut overflow
					nm[i][i+1] = overflow;
				}
			}
			printf("\n");
			printf("\n");
			for(int i=0;i<255;i++){
				printf("\n");
				for(int j=0;j<(nm[i][i])/4;j++) printf("#");
			}

			int cnt[255][255] = {};

			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
						idata.results[RED][y][x] = idata.source[RED][y][x];
						idata.results[GREEN][y][x] = idata.source[GREEN][y][x];
						idata.results[BLUE][y][x] = idata.source[BLUE][y][x];
				}
			}

			for(int x=0; x<255; x++){
				for(int y=0; y<255; y++){
					int g = idata.source[RED][y][x];
					int k = 0;
					for(; k<255; k++){
						if(nm[g][k] == 0) continue;
						if(cnt[g][k] < nm[g][k]){
							idata.results[RED][y][x] = k;
							idata.results[GREEN][y][x] = k;
							idata.results[BLUE][y][x] = k;
							cnt[g][k]++;
						}
					}

				}
			}

			if (writeBMPfile(argv[2], &idata) > 0)
				printf("コピー先ファイル%sに保存できませんでした\n",argv[2]);
		}
	}
}

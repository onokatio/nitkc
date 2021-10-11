#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#ifndef DEF_H

#include "def.h"
#define DEF_H

#endif
#include "var.h"

#include "bmpfile.h"

int compare(const void* a, const void* b){
	return *(double*)a - *(double*)b;
}

int avg(imgdata idata,int x, int y){
	int sum = 0;
	int sizex = 7;
	int sizey = 7;
	int pie = 0;
	for(int i=0; i<sizey ; i++){
		for(int j=0; j<sizex ; j++){
			if (y-1+i < 0){
				pie++;
				continue;
			}
			if (y-1+i > idata.height){
				pie++;
				continue;
			}
			if (x-1+j < 0){
				pie++;
				continue;
			}
			if (x-1+j > idata.width){
				pie++;
				continue;
			}
			sum += idata.source[RED][y-1+i][x-1+j];
		}
	}
	int avg = sum / (sizex * sizey - pie);
	return avg;
}
int alpha(imgdata idata,int x, int y){
	int sum = 0;
	int sizex = 7;
	int sizey = 7;
	int pie = 0;
	for(int i=0; i<sizey ; i++){
		for(int j=0; j<sizex ; j++){
			if (y-1+i < 0){
				pie++;
				continue;
			}
			if (y-1+i > idata.height){
				pie++;
				continue;
			}
			if (x-1+j < 0){
				pie++;
				continue;
			}
			if (x-1+j > idata.width){
				pie++;
				continue;
			}
			sum += idata.source[RED][y-1+i][x-1+j];
		}
	}
	int avg = sum / (sizex * sizey - pie);
	sum = 0;
	for(int i=0; i<sizey ; i++){
		for(int j=0; j<sizex ; j++){
			if (y-1+i < 0){
				pie++;
				continue;
			}
			if (y-1+i > idata.height){
				pie++;
				continue;
			}
			if (x-1+j < 0){
				pie++;
				continue;
			}
			if (x-1+j > idata.width){
				pie++;
				continue;
			}
			sum += (idata.source[RED][y-1+i][x-1+j] - avg)*(idata.source[RED][y-1+i][x-1+j] - avg);
		}
	}
	avg = sum / (sizex * sizey - pie);
	return avg;
}

int main(int argc, char *argv[])
{
	imgdata idata;
	int x, y;

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
			int histogram[256] = {};
			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
                                        idata.results[RED][y][x] = idata.source[RED][y][x];
                                        idata.results[RED][y+1][x] = idata.source[RED][y][x];
                                        idata.results[RED][y][x+1] = idata.source[RED][y][x];
                                        idata.results[RED][y+1][x+1] = idata.source[RED][y][x];
                                }
			}


			if (writeBMPfile(argv[2], &idata) > 0) printf("コピー先ファイル%sに保存できませんでした\n",argv[2]);
		}
	}
}

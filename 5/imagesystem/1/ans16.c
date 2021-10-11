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
			int max1 = 0;
			int max1_i = 0;
			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
					histogram[idata.source[RED][y][x]]++;
				}
			}
			for (int i = 0; i < 256; i++){
					if(histogram[i] > max1){
						max1 = histogram[i];
						max1_i = i;
					}
			}
			int max2 = 0;
			int max2_i = 0;
			for (int i = 0; i < 256; i++){
				if(abs(i - max1_i) < 50) continue;
				if(histogram[i] > max2){
					max2 = histogram[i];
					max2_i = i;
				}
			}
			int min = 255;
			int min_i = 0;
			int start,end;
			if (max1_i > max2_i){
				start = max2_i;
				end = max1_i;
			}else{
				start = max1_i;
				end = max2_i;
			}
			for (int i = start; i < end; i++){
					if(histogram[i] < min){
						min = histogram[i];
						min_i = i;
					}
			}
			printf("max1: %d %d\n", max1, max1_i);
			printf("max2: %d %d\n", max2, max2_i);
			printf("min: %d %d\n", min, min_i);
			/* 例題：コピーするプログラム */
			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
					if(idata.source[RED][y][x] >= min_i){
						idata.results[RED][y][x] = 255;
						idata.results[BLUE][y][x] = 255;
						idata.results[GREEN][y][x] = 255;
					}else{
						idata.results[RED][y][x] = 0;
						idata.results[BLUE][y][x] = 0;
						idata.results[GREEN][y][x] =  0;
					}
				}
			}


			if (writeBMPfile(argv[2], &idata) > 0) printf("コピー先ファイル%sに保存できませんでした\n",argv[2]);
		}
	}
}

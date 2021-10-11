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

int avg_calc(Uchar source[COLORNUM][MAXHEIGHT][MAXWIDTH],int x, int y){
	int sum = 0;
	int sizex = 7;
	int sizey = 7;
	int pie = 0;
	for(int i=0; i<sizey ; i++){
		for(int j=0; j<sizex ; j++){
			if (y-3+i < 0){
				pie++;
				continue;
			}
			if (y-3+i > 300){
				pie++;
				continue;
			}
			if (x-3+j < 0){
				pie++;
				continue;
			}
			if (x-3+j > 300){
				pie++;
				continue;
			}
			sum += source[RED][y-3+i][x-3+j];
		}
	}
	int avg = sum / (sizex * sizey - pie);
	return avg;
}

int alpha(Uchar source[COLORNUM][MAXHEIGHT][MAXWIDTH],int x, int y){
	int sum = 0;
	int sizex = 7;
	int sizey = 7;
	int pie = 0;
	for(int i=0; i<sizey ; i++){
		for(int j=0; j<sizex ; j++){
			if (y-3+i < 0){
				pie++;
				continue;
			}
			if (y-3+i > 300){
				pie++;
				continue;
			}
			if (x-3+j < 0){
				pie++;
				continue;
			}
			if (x-3+j > 300){
				pie++;
				continue;
			}
			sum += source[RED][y-3+i][x-3+j];
		}
	}
	int avg = sum / (sizex * sizey - pie);
	//int avg = 0;
	//avg = avg_calc(source,x,y);
	sum = 0;
	for(int i=0; i<sizey ; i++){
		for(int j=0; j<sizex ; j++){
			if (y-3+i < 0){
				pie++;
				continue;
			}
			if (y-3+i > 300){
				pie++;
				continue;
			}
			if (x-3+j < 0){
				pie++;
				continue;
			}
			if (x-3+j > 300){
				pie++;
				continue;
			}
			int n =(source[RED][y-3+i][x-3+j] - avg);
			sum += n*n;
		}
	}
	int al = sum / (sizex * sizey - pie);
	//printf("%d, ",avg);
	return al;
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
					printf("a");
		if (readBMPfile(argv[1], &idata) > 0)
			printf("指定コピー元ファイル%sが見つかりません\n",argv[1]);
		else {
			//int histogram[256] = {};
			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
						idata.cwork[RED][y][x] = 0;
						idata.cwork[BLUE][y][x] = 0;
						idata.cwork[GREEN][y][x] = 0;
				}
			}
			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
					if ( alpha(idata.source,x,y) >= 1000 ){
						idata.cwork[RED][y][x] = avg_calc(idata.source,x,y);
					}
					
				}
			}
			for (y = 0; y < idata.height; y++){
				for (x = 0; x < idata.width; x++){
                                        if(idata.source[RED][y][x] >= idata.cwork[RED][y][x]){
                                                idata.results[RED][y][x] = 255;
                                                idata.results[BLUE][y][x] = 255;
                                                idata.results[GREEN][y][x] = 255;
                                        }else{
                                                idata.results[RED][y][x] = 0;
                                                idata.results[BLUE][y][x] = 0;
                                                idata.results[GREEN][y][x] = 0;
                                        }
					/*
                                        idata.results[RED][y][x] = idata.cwork[RED][y][x];
                                        idata.results[BLUE][y][x] = idata.cwork[BLUE][y][x];
                                        idata.results[GREEN][y][x] = idata.cwork[GREEN][y][x];
					*/
                                }
			}


			if (writeBMPfile(argv[2], &idata) > 0) printf("コピー先ファイル%sに保存できませんでした\n",argv[2]);
		}
	}
}

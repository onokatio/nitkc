#include <stdio.h>
#include <stdlib.h>

#ifndef DEF_H

#include "def.h"
#define DEF_H

#endif
#include "var.h"

#include "bmpfile.h"

int main(int argc, char *argv[])
{
	imgdata idata;
	double c;
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
		/* 例題：コピーするプログラム */

		double Nroot = 3;
		double n = 5;
		double sum = 0;

		for (y = 0; y < idata.height; y++){
			for (x = 0; x < idata.width; x++){
				int skip = 0;
				sum = 0;

				for (int j = 0; j < Nroot; j++){
					for (int i = 0; i < Nroot; i++){
						int relative_x = i - (Nroot-1)/2;
						int relative_y = j - (Nroot-1)/2;
						if(y + relative_y < 0 
						|| y + relative_y >= idata.height
						|| x + relative_x < 0
						|| x + relative_x >= idata.width ){
							skip++;
							continue;
						}
						if(relative_x == 0 && relative_y == 0){
							sum += idata.source[RED][y + relative_y][x + relative_x] * n;
						}else{
							sum += idata.source[RED][y + relative_y][x + relative_x];
						}
					}
				}
				int tmpN = Nroot*Nroot - skip;
				double color = sum / (tmpN-1.0+n);
				idata.results[RED][y][x] = color;
				idata.results[GREEN][y][x] = color;
				idata.results[BLUE][y][x] = color;
			}
		}


		if (writeBMPfile(argv[2], &idata) > 0) printf("コピー先ファイル%sに保存できませんでした\n",argv[2]);
	}
}
}

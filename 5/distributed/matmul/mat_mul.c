#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <omp.h>
#include "mat_mul.h"


/* a,b を単位行列に初期化 */
void
mat_set(double a[N][N],double b[N][N])
{
	int i,j;
	double d;

	for (i = 0;i < N;i++){
		for (j = 0;j < N;j++){
			d = 0.0;
			if (i == j){
				d = 1.0;
			}
			a[i][j] = d;
			b[i][j] = d;
		}
	}
}

/* a,b をランダムな行列に初期化 */
void
mat_set_random(double a[N][N],double b[N][N])
{
	int i,j;
	double d;

	for (i = 0;i < N;i++){
		for (j = 0;j < N;j++){
			a[i][j] = ((double) random()) / INT_MAX;
			b[i][j] = ((double) random()) / INT_MAX;
		}
	}
}

/* 正方行列の積を計算する c = a * b */
void
mat_mul(double a[N][N], double b[N][N], double c[N][N],int n)
{
	int i,j,k;

	/* for ループを並列化する．						*/
	/* 変数 j, k はスレッドごとに別々のものを持つ．	*/
	#pragma omp parallel for private(j,k)
	for(i = 0;i < n;i++) {
		for(j = 0;j < n;j++) {
			c[i][j] = 0.0;
			for(k = 0;k < n; k++) {
				c[i][j] += a[i][k] * b[k][j];
			}
		}
	}
}

/* 行列を表示する */
void
mat_show(double c[N][N])
{
	int i,j,n;

	if (N > 10){
		n = 10;
	}else{
		n = N;
	}
	for (i = 0;i < n;i++){
		for (j = 0;j < n;j++){
			printf ("%2.1f ",c[i][j]);
		}
		if (N > n){
			printf("…");
		}
		printf("\n");
	}
	if (N > n){
		printf("…\n");
	}
}

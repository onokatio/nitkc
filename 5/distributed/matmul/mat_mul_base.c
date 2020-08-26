#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <omp.h>

#define N	(1000LL)

static void
mat_set(double m[N][N]);

extern void
mat_set_random(double m[N][N]);

static void
mat_mul(double a[N][N], double b[N][N], double c[N][N],int n);

static void
mat_show(double c[N][N]);

int
mat_is_identity(double a[N][N],int n);

int main(void){
	static double a[N][N],b[N][N],c[N][N];
	double ts,te;

	mat_set(a);
	mat_set(b);
	ts = omp_get_wtime();
	mat_mul(a,b,c,N);
	te = omp_get_wtime();
	printf("N=%lld time %.2fs\n",N, te - ts);
	if (mat_is_identity(a,N) && mat_is_identity(b,N)){
		if (mat_is_identity(c,N)){
			printf("おめでとう! 単位行列×単位行列 = 単位行列　になりました\n");
			printf("ただし，プログラムの正しさが完全に確かめられたわけではありません\n");
		}else{
			printf("プログラムがまちがっているかも... 単位行列同士の積が単位行列になりませんでした\n");
		}
	}
	//mat_show(c,N);
}

void
mat_set(double m[N][N])
{
	int i,j;
	double d;

	for (i = 0;i < N;i++){
		for (j = 0;j < N;j++){
			/* テスト用 */
			if (i == j){
				d = 1.0;
			}else{
				d = 0.0;
			}
			/* ランダムデータ */
			//d = ((doulble)random() / INT_MAX) * 10.0;
			m[i][j] = d;
		}
	}
}

/* a,b をランダムな行列に初期化 */
void
mat_set_random(double m[N][N])
{
	int i,j;
	double d;

	for (i = 0;i < N;i++){
		for (j = 0;j < N;j++){
			m[i][j] = ((double) random()) / INT_MAX;
		}
	}
}

void
mat_mul(double a[N][N], double b[N][N], double c[N][N],int n)
{
	int i,j,k;

	/*
	for(i = 0;i < n;i++) {
		for(j = 0;j < n;j++) {
			c[i][j] = 0;
		}
	}
	*/

	/* for ループを並列化する．*/
	/* 変数 j, k はスレッドごとに別々のものを持つ．	*/
	#pragma omp parallel for private(j,k)
	for(i = 0;i < n;i++) {
		for(j = 0;j < n;j++) {
			c[i][j] = 0.0;
			for(k = 0;k < n; k++) {
				c[i][j] = c[i][j] + a[i][k] * b[k][j];
			}
		}
	}
}

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

int
mat_is_identity(double a[N][N],int n)
{
	int i,j;

	for (i = 0;i < n;i++){
		for (j = 0;j < n;j++){
			if ((i == j && a[i][j] != 1.0) || (i != j && a[i][j] != 0.0)){
				return (0);
			}
		}
	}
	return (1);
}

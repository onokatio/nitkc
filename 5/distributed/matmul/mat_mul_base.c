#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <x86intrin.h>
#include <omp.h>

#define N	(1000LL)
#define USE_TRANSPOSE
#define USE_FMA
#define USE_OMP

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
	static double __attribute__((aligned(32))) a[N][N],b[N][N],c[N][N];
	double ts,te;

	mat_set_random(a);
	mat_set_random(b);
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
	mat_show(c);
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

void
mat_transpose(double m[N][N])
{
	int i,j;
	double n[N][N];

	for (i = 0;i < N;i++){
		for (j = 0;j < N;j++){
			n[j][i] = m[i][j];
		}
	}

	for (i = 0;i < N;i++){
		for (j = 0;j < N;j++){
			m[i][j] = n[i][j];
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
	int tmpk,tmpj;

	/*
	for(i = 0;i < n;i++) {
		for(j = 0;j < n;j++) {
			c[i][j] = 0;
		}
	}
	*/

#ifdef USE_TRANSPOSE
	mat_transpose(b);
#endif
	/* for ループを並列化する．*/
	/* 変数 j, k はスレッドごとに別々のものを持つ．	*/
	#pragma omp parallel for private(j,k) num_threads(8)
	for(i = 0;i < n;i++) {
		for(j = 0;j < n;j++) {
			c[i][j] = 0.0;
			for(k = 0;k < n; k++) {
#ifdef USE_TRANSPOSE
				tmpk = j;
				tmpj = k;
#else
				tmpk = k;
				tmpj = j;
#endif

#ifdef USE_FMA
				c[i][j] = fma(a[i][k],b[tmpk][tmpj],c[i][j]);
#elif defined USE_AVX
				double __attribute__((aligned(32))) a1 = a[i][k];
				double __attribute__((aligned(32))) b1 = b[tmpk][tmpj];
				double __attribute__((aligned(32))) c1 = c[i][j];
				__m256d A = _mm256_set_pd(a1,a1,a1,a1);
				__m256d B = _mm256_set_pd(b1,b1,b1,b1);
				__m256d C = _mm256_set_pd(c1,c1,c1,c1);
				__m256d tmp = _mm256_mul_pd(A,B);
				__m256d tmp2 = _mm256_add_pd(C,tmp);
				double __attribute__((aligned(32))) ans[4];
				_mm256_store_pd(ans,tmp2);
				c[i][j] += ans[0];
#else
				c[i][j] += a[i][k] * b[tmpk][tmpj];
#endif
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

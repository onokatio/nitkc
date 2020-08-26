#include <stdio.h>
#include <limits.h>

#define N	(10LL)


static void
mat_set(double m[N][N]);

static void
mat_mul(double a[N][N], double b[N][N], double c[N][N],int n);

static void
mat_show(double c[N][N]);

int main(void){
    static double a[N][N],b[N][N],c[N][N];
    double ts,te;

    mat_set(a,N);
    mat_set(b,N);
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

void
mat_mul(double a[N][N], double b[N][N], double c[N][N],int n)
{
	int i,j,k;

	for(i = 0;i < n;i++) {
		for(j = 0;j < n;j++) {
			c[i][j] = 0;
		}
	}

	for(i = 0;i < n;i++) {
		for(j = 0;j < n;j++) {
			for(k = 0;k < n; k++) {
				c[i][j] = c[i][j] + a[i][k] * b[k][j];
			}
		}
	}
}

void
mat_show(double c[N][N])
{
	int i,j;

	for (i = 0;i < N;i++){
		for (j = 0;j < N;j++){
			printf ("%2.1lf ",c[i][j]);
		}
		printf("\n");
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

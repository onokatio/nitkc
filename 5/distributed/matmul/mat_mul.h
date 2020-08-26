#ifndef MAT_MUL_H_INCLUDED
#define MAT_MUL_H_INCLUDED

#ifndef N
	#define N	(16LL)
#endif

extern void
mat_set(double a[N][N],double b[N][N]);

extern void
mat_set_random(double a[N][N],double b[N][N]);

extern void
mat_mul(double a[N][N], double b[N][N], double c[N][N],int n);

extern void
mat_show(double c[N][N]);

#endif

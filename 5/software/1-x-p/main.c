#include <stdio.h>

int main(void){
	double num;
	printf("input x: ");
	scanf("%lf", &num);

	double eps = 0.0000001;
	double a = 1.0 - num;
	while( 1.0 - (a+1.0)*num > eps ){
		a = (1.0-num)*(1.0+a);
		printf("an = %lf\n", a+1.0);
	}
	printf("1/x = %lf\n", a+1.0);
}


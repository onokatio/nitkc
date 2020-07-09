#include <stdio.h>
#include <time.h>
#include <omp.h>

int main(void){
	int i,s = 0;
	omp_set_num_threads(2);
	#pragma omp parallel for
	for (i = 0; i < 100000; i++) {
		usleep(1);
		s++;
	}
	printf("%d\n",s);
}

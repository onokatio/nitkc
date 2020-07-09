#include <stdio.h>
#include <time.h>
#include <omp.h>

int main(void){
	int i,s = 0;
	omp_lock_t lock;
	omp_init_lock(&lock);

	omp_set_num_threads(2);

	#pragma omp parallel for
	for (i = 0; i < 100000; i++){
		omp_set_lock(&lock);
		s++;
		omp_unset_lock(&lock);
	}
	printf("%d\n",s);
}

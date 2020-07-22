#include <stdio.h>
#include <omp.h>

int main(void){
	#pragma omp parallel
	{
		printf("id=%d\n", omp_get_thread_num());
	}
}

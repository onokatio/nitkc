mat_mul : mat_mul_base.c
	#gcc -O0 -Wall -march=native -mfma -mavx2 -lm -fopenmp $^ -o $@
	gcc -mcmodel=large -flto -Ofast -ffast-math -Wall -mtune=native -march=native -mfma -mavx2 -lm -fopenmp $^ -o $@

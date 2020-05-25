#include <stdio.h>

#define bool int
#define true 1
#define false 0

void main(){
	int number;
	bool done;
	number = 1;
	done = false;
	while(number<=10){
		printf("next integer:");
		printf("%d\n",number);
		number++;
	}
	while(! done){
		printf("next integer:");
		printf("%d\n",number);
		number++;
		if(number==21) done = true;
	}
}

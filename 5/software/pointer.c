#include <stdio.h>

void string_copy(char *str1, char *str2){
    while( (*(str2++) = *(str1++)) );
}

void string_concat(char *str1, char *str2){
    while(*(str1++));
    string_copy(str2,str1-1);
}

int main(){
	char hello[] = "hello";
	char string[10];

	string_copy(hello, string);

	printf("hello: %s\n", hello);
	printf("string: %s\n", string);

	char concat_first[20] = "first";
	char concat_second[] = "second";

	string_concat(concat_first, concat_second);

	printf("concat: %s", concat_first);
	
	return 0;
}

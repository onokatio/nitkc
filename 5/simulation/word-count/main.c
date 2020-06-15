#include <stdio.h>

int main(int argc, char *argv[]){
	FILE *fp = fopen(argv[1], "r");
	char ch;
	int cc = 0;
	int lc = 0;
	int wc = 0;
	while( (ch = getc(fp)) != EOF ){
		printf("%c",ch);
		if( 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || '0' <= ch && ch <= '9' ){
			cc++;
		}else if(ch == '\n'){
			lc++;
		}else if(ch == ' ' ){
			wc++;
		}
	}

	printf("char = %d, word = %d, line = %d", cc, wc, lc);

	return 0;
}

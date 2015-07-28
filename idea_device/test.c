# include <stdio.h>
# include <stdlib.h>

void printBinaryOfChar(char c) {
	int i;
	for (i = 7; i >= 0; --i) {
		putchar( (c & (1 << i)) ? '1' : '0' );
	}
	printf("\n");
}

void printBinaryOfLong(long c) {
	int i;
	for (i = 31; i >= 0; --i) {
		putchar( (c & (1 << i)) ? '1' : '0' );
	}
	putchar('\n');
}


void printWholeLine() {
	int c;
	while (1) {
		scanf("%d", &c);
		if (c == EOF) {
			break;
		}
		printf("%c", (char) c);
	}
}


/**
	len contains the number of bytes allocated
*/
void readLineGetLine() {
	char *line = NULL;
	size_t len=0;
	size_t len_ret = getline(&line, &len, stdin);
	// printf("%s", line);
	printf("\nlen: %d\nreturned: %d\n", len, len_ret);
	int i=0;
	while (line[i] != '\t') {
		printBinaryOfChar(line[i]);
		i++;
	}
}


int main() {
	long c;
	readLineGetLine();
	// while (1) {
		// c = getc(stdin);
		// if (c == EOF) {
			// break;
		// }
		// putc(c, stdout);
	// }
	// char str[30];
	// scanf("%s", str);
	// printf("%s", str);
}

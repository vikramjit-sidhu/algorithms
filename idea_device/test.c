
# include <stdio.h>

void printBinaryOfChar(char ch) {
	int i;
	for (i = 0; i < 8; i++) {
		printf("%d", !!((ch << i) & 0x80));
	}
	printf("\n");
}

void printBinaryOfChar2(char c) {
	for (int i = 7; i >= 0; --i) {
		putchar( (c & (1 << i)) ? '1' : '0' );
	}
	putchar('\n');
}


int main() {
	int c;
	char ch;
	while (1) {
		c = getchar();
		if (c == EOF) {
			break;
		}
		putchar(c);
		scanf("%c", &ch);
		printf("%c->", ch);
		// if (ch == '\n') {
		// 	printf("\n");
		// 	continue;
		// }
		printBinaryOfChar2(ch);
	}
}

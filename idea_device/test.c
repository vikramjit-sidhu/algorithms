# include <stdio.h>
# include <stdlib.h>

void printBinaryOfChar(char c) {
	int i;
	for (i = 7; i >= 0; --i) {
		putchar( (c & (1 << i)) ? '1' : '0' );
	}
	printf("\n");
}


char *getBinaryOfChar(char c) {
	int i, j;
	char *binary_repr = (char *) malloc(8*sizeof(char));
	for (i = 7, j = 0; i >= 0; --i, j++) {
		binary_repr[j] = (c & (1 << i)) ? '1' : '0';
	}
	return binary_repr;
}

/**
	len contains the number of bytes allocated dynamically to line
	return value of getline will be -1 if EOF is reached
*/
char *readLineGetLine(size_t *chars_read_pointer) {
	char *line = NULL;
	size_t space_allocated = 0;
	*chars_read_pointer = getline(&line, &space_allocated, stdin);
	// printf("\nlen: %d\nreturned: %d\n", len_pointer, len_ret);
	// printf("%s", line);
	return line;
}


int countNumBytesInUtf8Char(char *first_byte_in_binary) {
	int num_bytes = 0, index = 0;
	while (first_byte_in_binary[index] != '0') {
		num_bytes++;
		index++;
	}
	return num_bytes;
}

void pointerRevision(char *str) {
	char *freeing = str;
	freeing++;
	// free(str);
	while (*free != NULL) {
		printf("%c", *freeing);
		freeing++;
	}
}

// int main() {
// 	char *str = "111100000";
// 	printf("%d", countNumBytesInUtf8Char(str));
// 	return 0;
// }


// int main() {
// 	char *binary = getBinaryOfChar('a');
// 	printf("%s\n", binary);
// 	binary = getBinaryOfChar('K');
// 	printf("%s\n", binary);
// 	return 0;
// }


// int main() {
// 	while (1) {
// 		size_t chars_read;
// 		char *line = readLineGetLine(&chars_read);
// 		if (chars_read == -1) {
// 			break;
// 		}
// 		int i=0;
// 		while (line[i] != NULL) {
// 			printf("\nindex:%d %s", i, getBinaryOfChar(line[i]));
// 			i++;
// 		}
// 		free(line);
// 		printf("\n%s\n\n", line);
// 	}
// }

int main() {
	size_t chars_read;
	char *str = readLineGetLine(chars_read);
	pointerRevision(str);

	return 0;
}

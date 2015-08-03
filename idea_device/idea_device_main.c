/**
Idea device problem statement:

UTF-8 is probably the most common unicode encoding scheme in the world. UTF-8 is designed to retain the extremely widespread 7-bit ASCII encoding without any change. 
This is probably the biggest reason for UTF-8's popularity.

Your objective is to write a C program that reads multiple UTF-8 encoded strings from STDIN (1 string per line), 
count all non-ascii characters (ascii characters are with ordinal decimal 0 to 127) and print the total non-ascii character count to STDOUT (1 number per line).

Note that:
    You cannot use any wchar.h service in your program. This rule will disqualify your program even if you generate the right result.
    The UTF-8 strings supplied to you can have 1 or more whitespaces in them.
    No input string will have a character length greater than 200 (including spaces)
    You will be given multiple lines of input (1 string per line).
    Input will be limited to UTF-8 encoded strings and will not contain any garbage values.
	
We will test your program by compiling it on Linux and running it as follows.

$ gcc your_prog.c -Wall
$ ./a.out < test_cases > generated_output
$ diff -B --strip-trailing-cr generated_output correct_output
*/

# include <stdio.h>
# include <stdlib.h>

# define NUM_BITS_IN_BYTE 8

/**	Reads a line from stdin and returns it to calling function in line variable
*	End of a line is denoted by NULL variable
*	The getline function returns -1 if EOF is reached, or it returns number of chars read
*	setting this value to pointer chars_read_pointer, which is then used by calling function to check for EOF
*/
char *readLine(size_t *chars_read_pointer) {
	char *line = NULL;
	size_t space_allocated = 0;
	*chars_read_pointer = getline(&line, &space_allocated, stdin);
	return line;
}

/**	Given a char c, return its binary representation.
*	char data type in C is of 8 bits or 1 byte.
*/
char *getBinaryOfChar(char c) {
	int i, j;
	char *binary_repr = (char *) malloc(NUM_BITS_IN_BYTE * sizeof(char));
	for (i = 7, j = 0; i >= 0; --i, j++) {
		binary_repr[j] = (c & (1 << i)) ? '1' : '0';
	}
	return binary_repr;
}

/**	Given binary representation of char, returns 1 if it is a Non-ASCII char, 0 otherwise
*	ASCII chars are represented in 8 bits, and have first bit 0 :  0xxxxxxx
*	All other non-ASCII, UTF-8 characters have the first bit set to 1
*/
int isNonAsciiChar(char *char_in_binary) {
	if (char_in_binary[0] == '1') {
		return 1;
	}
	return 0;
}

/**	Given binary representation of first byte of a UTF-8 char, returns total bytes for utf-8 char.
*	All utf-8 encoded characters contain the total number of bytes encoded in the first byte
*	eg. if there are 2 bytes in encoding, it will be of form: 110xxxxx 10xxxxxx
*	For more details refer: https://en.wikipedia.org/wiki/UTF-8#Description
*/
int countNumBytesInUtf8Char(char *first_byte_in_binary) {
	int num_bytes = 0, index = 0;
	while (first_byte_in_binary[index] != '0') {
		num_bytes++;
		index++;
	}
	return num_bytes;
}


int main() {
	while (1) {
		size_t chars_read_in_line = 0;
		/* Passing pointer to get no of chars read in var, it will be -1 if EOF reached	*/
		char *line = readLine(&chars_read_in_line);
		if (chars_read_in_line == -1) {
			break;
		}
		int i = 0;	//Index variable for iterating chars in line
		int count_non_ascii_chars = 0;
		/* The line returned by getLine(..) function is NULL terminated, 
		it also has \n before NULL, but since \n is an ASCII char, it does not affect program output */
		while (line[i] != NULL) {
			char *binary_of_char = getBinaryOfChar(line[i]);
			if (isNonAsciiChar(binary_of_char) == 1) {
				/* Incrementing count of non-ASCII chars */
				count_non_ascii_chars++;
				int num_bytes_in_utf8_char = countNumBytesInUtf8Char(binary_of_char);
				/* Advancing the index ahead by the number of bytes that the current utf-8 char is represented in */
				i += num_bytes_in_utf8_char;
				free(binary_of_char);
				continue;
			}
			free(binary_of_char);
			i++;
		}
		printf("%d\n", count_non_ascii_chars);	//Outputting num of non-ascii chars
	}
	
	return 0;	//Successful completion of program
}

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

/**	Checks if char1 is the EOF special character, EOF is an integer value
*	Return value 0-False; 1-True
*/
int charIsEOF(char char1) {
	if (char1 == EOF) {
		return 1;
	}
	return 0;
}

/**	Checks if the char passed as an argument (@param charToCheck) is an ASCII character
*	@param returnValue This method return 0 if charToCheck is NOT and ASCII character, 1 is returned if it IS and ASCII char
*/
// int isAsciiChar(char charToCheck) {
	// int returnValue = 0, asciiValueOfChar;
	// asciiValueOfChar = int (charToCheck);
	// if asciiValueOfChar 
// }

/**	Counts the number of non-ASCII characters in a line
*	Reads a line of text character by character until a new line (\n) delimitor is found
*	As each character is read, a method is called to check if it is an ASCII character, if not, a count is incremented
*	@param nonAsciiChars contains the number of non-ASCII characters in the line, this variable is returned from this method
*/
int countAsciiCharsInLine() {
	int nonAsciiChars = 0;
	/* The current character of the line which is being processed */
	int currentCharInLine;
	while (1) {
		scanf("%d", &currentCharInLine);
		/* Checking if this character is the EOF, returning to the calling function in that case */
		if (charIsEOF(currentCharInLine) == 1) {
			return -1;
		}
		/* The end of a line is denoted by \n */
		if ((char) 	currentCharInLine == '\n') {
			break;
		}
		printf("%d ", currentCharInLine);
	}
	return nonAsciiChars;
}


int main() {
	int nonAsciiChars;
	while (1) {
		nonAsciiChars = countAsciiCharsInLine();
		/* Check if EOF is reached, return value from function is -1 in that case and program exits */
		if (nonAsciiChars < 0) {
			break;
		}
		// printf("\n%d", nonAsciiChars);
	}
	
	return 0;	//Successful completion of program
}

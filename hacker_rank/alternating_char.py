"""
Hacker rank alternating characters
https://www.hackerrank.com/challenges/alternating-characters
"""

def alternate_char(inp_str):
    """ Adjacent characters in inp_str have to be different, can only be achieved by deleting char """
    clean_str = ''
    curr_index = 0
    clean_str += inp_str[curr_index]
    len_str = len(inp_str)
    del_req = 0
    while curr_index < len_str:
        next_index = curr_index + 1
        while next_index < len_str and inp_str[next_index] == inp_str[curr_index]:
            del_req += 1
            next_index += 1
        if next_index >= len_str:
            break
        clean_str += inp_str[next_index]
        curr_index = next_index
    return del_req

def main():
    test_cases = int(input().strip())
    for i in range(test_cases):
        inp_str = input().strip()
        print(alternate_char(inp_str))

if __name__ == '__main__':
	main()
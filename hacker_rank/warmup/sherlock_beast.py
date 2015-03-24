"""
Hacker Rank - Sherlock and Beast
https://www.hackerrank.com/challenges/sherlock-and-the-beast
"""

def generate_niceness(num_digits):
    num_5dig = num_digits
    num_3dig = 0
    while (num_5dig % 3) != 0:
        num_5dig -= 5
        if num_5dig < 0:
            return -1
        num_3dig += 5
    return '5'*num_5dig + '3'*num_3dig

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        num_digits = int(input().strip())
        print(generate_niceness(num_digits))

if __name__ == '__main__':
    main()
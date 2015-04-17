"""
Hacker Rank - Antipalindromic Strings
https://www.hackerrank.com/challenges/antipalindromic-strings
"""

def main():
    num_cases = int(input().strip())
    num = pow(10,9) + 7
    for i in range(num_cases):
        #m -> size of alphabet set (consider a new alphabet set whose size can be greater than 26)
        #n -> length of strings
        n, m = (int(i) for i in input().strip().split(' '))
        if n == 1:
            num_antipalins = m
        elif m == 1:
            num_antipalins = 0
        else:
            num_antipalins = (pow(m-2, n-2, num) * m * (m-1)) % num
        print(num_antipalins)
        
if __name__ == '__main__':
    main()
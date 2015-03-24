"""
Hacker rank challenge
flipping bits
https://www.hackerrank.com/challenges/flipping-bits
"""

#flips bits of 32 bit unsigned integers
flip_bits = lambda a: a^4294967295

def main():
    n = int(input())
    for i in range(n):
        print(flip_bits(int(input().strip())))
    
if __name__ == '__main__':
    main()
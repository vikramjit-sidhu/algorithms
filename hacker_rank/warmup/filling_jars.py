"""
Hacker rank - Filling jars
https://www.hackerrank.com/challenges/filling-jars
"""

def main():
    n, m = [int(i) for i in input().strip().split(' ')]
    tot = 0
    for i in range(m):
        a, b, k = [int(i) for i in input().strip().split(' ')]
        tot += (b - a + 1) * k
    print(tot // n)

if __name__ == '__main__':
    main()
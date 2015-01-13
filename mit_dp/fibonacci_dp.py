"""
DP version of fibonacci number computation
"""

MEMO = {}   #memoized table

def main():
    n = int(input("enter range of fibonacci number computation(n): "))
    fi = fib(n)
    print ("fibonacci number is: {}".format(fi))


def fib(n):
    if n in MEMO:
        return MEMO[n]
    if n <= 2:
        f = 1
    else:
        f = (fib(n-1) + fib(n-2))
    MEMO[n] = f
    return f



if __name__ == '__main__':
    main()

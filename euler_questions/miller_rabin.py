"""
miller rabin primality test, checking remainders
"""
from math import ceil, log


def main():
    n = int(input("number for primality check: "))
    print("RESULT: {}".format(primality_test(n)))



def primality_test(n):
    """
    miller rabin primality test used
    n-1 = 2^s * d
    """
    print("testing primality of {}".format(n))
    n = int(n)

#finding s and d    
    num = n-1
    s = ceil(log(n, 2))
    power = pow(2, s)
    while (num % power) != 0:
        s -= 1
        power = int(power/2)
    d = int(num/power)  #computing d, after obtaining 2^s

    strong_pseudoprimes = [2, 3, 31, 73, 5, 7, 61, 11, 13, 17, 19, 23, 1662803]
    prime = True
    for a in strong_pseudoprimes:
        x = pow(a, d, n)
        if x == 1 or x == num:
            continue
            
        found = False
        for i in range(1, s):
            x = pow(x, 2, n)
            if x == num:
                found = True
                break
            elif x == 1:
                prime = False
                break

        if not prime:
            break
        elif not found:
            prime = False
            break

    return prime
    
    
    
if __name__ == '__main__':
    main()
    
"""
Euler q'n 3, finding largest prime factor of a number, n (600851475143)
https://projecteuler.net/problem=3

Using The sieve of Eratosthenes http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Finding all prime factors in a range (till sq rt n) then dividing them with n (INEFFICIENT METHOD)

Using Pollard Rho method to find factorization of number
http://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm

Miller Rabin Primality test used
http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""

from math import log, ceil, sqrt
from random import randint


def main():
#method1:
    # dividing_list_primes()

    #method2:
    n = int(input("enter the number to find largest prime factor of: "))

    factor1, factor2 = pollard_rho(n)
    
    print("factor1: {} and factor2: {}".format(factor1, factor2))

    if factor2 > factor1 and primality_test(factor2):
        print("\nlargest prime factor of {} is {}".format(n, factor2))
        return
    
    print("\nlargest prime factor of {} is {}".format(n, factor1))
    #factor1, factor2 = pollard_rho(n)


def pollard_rho(n):
    x = 2; y = 2; d = 1

    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x-y), n)

    if d == n:
        return (1, n)

    factor1 = d
    factor2 = int(n/d)
    return (factor1, factor2)



def primality_test(n):
    """
    miller rabin primality test used
    n-1 = 2^s * d
    """
    print("finding primality test of {}".format(n))
    n = int(n)
    
    s = ceil(log(n, 2))
    num = n-1
    while (num % pow(2, s)) != 0:
        s-=1
    d = int(num/pow(2, s))

    prime = True
    strong_pseudoprimes = [2, 3, 31, 73, 5, 7, 61, 11, 13, 17, 19, 23, 1662803]
    
    for a in strong_pseudoprimes:
        x = pow(a, d, n)
        if x == 1:
            continue
        for i in range(1, s-1):
            x = x*x
            if (x % n) == 1:
                prime = False
                break
            elif (x % n) == num:
                continue

        if not prime:
            break

    return prime



def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)


def g(x, n):
    return (x*x + 1) % n


#METHOD 2

def dividing_list_primes():
    n = int(input("enter the number to find largest prime factor of: "))
    prime_nos = generate_list_primes(n)

    for num in reversed(prime_nos):
        if n%num == 0:
            print("largest prime factor of {} is {}".format(n, num))
            return



def generate_list_primes(n):
    prime_nos = []
    limit = int(sqrt(n))

    numbers = list(range(3, limit+1, 2))
    prime_nos.append(2)

    for p in numbers:
        prime_nos.append(p)
        print("prime {} appended to list".format(p))
        num = p*p; inc = 2*p
        while num < limit:
            if num in numbers:
                numbers.remove(num)
            num += inc

    print ("final prime_nos list generated {}".format(prime_nos))
    return prime_nos




if __name__ == '__main__':
    main()

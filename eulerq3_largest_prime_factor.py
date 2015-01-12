"""
Euler q'n 3, finding largest prime factor of a number, n (600851475143)
https://projecteuler.net/problem=3

Using The sieve of Eratosthenes http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Finding all prime factors in a range (till sq rt n) then dividing them with n (INEFFICIENT METHOD)

Using Pollard Rho method to find factorization of number
http://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
"""

# from math import sqrt

def main():
    # dividing_list_primes()
    pollard_rho()



def pollard_rho():
    n = int(input("enter the number to find largest prime factor of: "))

    x = 2; y = 2; d = 1

    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x-y), n)
        print("{}   {}  {}".format(x, y, d))

    if d == n:
        return 1

    factor1 = d
    factor2 = n/d

    if factor2 > factor1 and primality_test(factor2):
        print("largest prime factor of {} is {}".format(n, factor2))
        return factor2

    print("largest prime factor of {} is {}".format(n, factor1))
    return factor1


def primality_test(num):
    


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)


def g(x, n):
    return (x*x + 1) % n




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

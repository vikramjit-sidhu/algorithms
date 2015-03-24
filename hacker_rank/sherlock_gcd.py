"""
Hacker Rank - Sherlock and GCD
https://www.hackerrank.com/challenges/sherlock-and-gcd
"""

def find_gcd(a, b):
    modulus = a % b
    if modulus == 0:
        return b
    return find_gcd(b, modulus)
    
def subset_exists(num_list):
    for index, i in enumerate(num_list):
        for j in num_list[index:]:
            gcd = find_gcd(i, j)
            if gcd == 1:
                return True
    return False
        
def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        len_list = int(input().strip())
        num_list = [int(j) for j in input().strip().split(' ')]
        if subset_exists(num_list):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
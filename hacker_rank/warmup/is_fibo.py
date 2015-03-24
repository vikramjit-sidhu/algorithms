"""
Hacker Rank - IsFibo
https://www.hackerrank.com/challenges/is-fibo
"""

from collections import OrderedDict

def generate_fibo(max):
    fibo_dict = {}
    prev, next = 0, 1
    while next < max:
        prev, next = next, next+prev
        fibo_dict[next] = True
    return fibo_dict

def main():
    max = 0 #the max number of inputs (fibo series will be generated only till here)
    num_list = []
    num_cases = int(input().strip())
    for i in range(num_cases):
        num = int(input().strip())
        if num > max:
            max = num
        num_list.append(num)
    fibo_dict = generate_fibo(max)
    for val in num_list:
        if val in fibo_dict:
            print("IsFibo")
        else:
            print("IsNotFibo")
    
if __name__ == '__main__':
    main()
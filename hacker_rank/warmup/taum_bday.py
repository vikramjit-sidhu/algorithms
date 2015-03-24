"""
Hacker Rank - Service Lane
https://www.hackerrank.com/challenges/service-lane
"""

def main():
    num_cases = int(input().strip())
    for y in range(num_cases):
        b, w = (int(x) for x in input().strip().split(' '))
        i, j, k = (int(x) for x in input().strip().split(' '))
        cost_blk = min(i, j+k)
        cost_white = min(j, i+k)
        spent = cost_blk*b + cost_white*w
        print(spent)
    
if __name__ == '__main__':
	main()
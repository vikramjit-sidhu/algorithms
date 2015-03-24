"""
Hacker Rank - Angry Professor
https://www.hackerrank.com/challenges/angry-professor
"""

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n, k = (int(i) for i in input().strip().split(' '))
        studt_times = [int(i) for i in input().strip().split(' ')]
        num_ontime = 0
        for time in studt_times:
            if time <= 0:
                num_ontime += 1
        if num_ontime >= k:
            print("NO")
        else:
            print("YES")

if __name__ == '__main__':
    main()
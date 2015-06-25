"""
Hacker Rank - Connected Cells
https://www.hackerrank.com/challenges/connected-cell-in-a-grid
"""

def main():
    rows = int(input().strip())
    cols = int(input().strip())
    matrix = []
    for i in range(rows):
        matrix.append([int(i) for i in input().strip().split(' ')])
    
        
if __name__ == '__main__':
    main()
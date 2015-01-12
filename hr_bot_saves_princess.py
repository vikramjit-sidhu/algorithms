"""
Hacker Rank Question Bot Saves princess
https://www.hackerrank.com/challenges/saveprincess
"""

def displayPathtoPrincess(n,grid):
    x, y = find_char_grid(grid, 'p')
    a, b = find_char_grid(grid, 'm')
    calculate_moves(x, y, a, b)

    
def calculate_moves(prinx, priny, botx, boty):
    print("princess:({}, {})  Bot:({},{})".format(prinx, priny, botx, boty))
    if priny < boty:
        print("UP")
        calculate_moves(prinx, priny, botx, boty-1)
    elif priny > boty:
        print("DOWN")
        calculate_moves(prinx, priny, botx, boty+1)
    elif prinx < botx:
        print("LEFT")
        calculate_moves(prinx, priny, botx-1, boty)
    elif prinx > botx:
        print("RIGHT")
        calculate_moves(prinx, priny, botx+1, boty)
    else:
        return
    
    
def find_char_grid(grid, char):
    for index, line in enumerate(grid):
        x = line.find(char)
        if x != -1:
            return (x, index)
    
    
def main():
    m = int(input())
    grid = [] 
    for i in range(0, m): 
        grid.append(input().strip())

    displayPathtoPrincess(m,grid)



if __name__ == '__main__':
    main()
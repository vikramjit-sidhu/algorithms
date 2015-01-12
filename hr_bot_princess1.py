"""
HackerRank Bot saves princess
https://www.hackerrank.com/challenges/saveprincess
"""


def displayPathtoPrincess(n,grid):
    x,y = find_princess_location(grid)
    a,b = find_bot_location(grid)
    if a<x:
        print("DOWN")
    elif a>x:
        print("UP")
    if b<y:
        print("RIGHT")
    elif b>y:
        print("LEFT")



def find_princess_location(grid):
    for index, row in enumerate(grid):
        y = row.find('p')
        if y>=0:
            return (index, y)


def find_bot_location(grid):
    for index, row in enumerate(grid):
        y = row.find('m')
        if y>=0:
            return (index, y)


def main():
    m = int(input())
    grid = [] 
    for i in range(0, m): 
        grid.append(input().strip())

    displayPathtoPrincess(m,grid)


if __name__ == '__main__':
    main()

#hacker rank question AI
#bot and princess 2
#https://www.hackerrank.com/challenges/saveprincess2



def nextMove(n,r,c,grid):
    x, y = find_princess(grid)
    if (c-y) > 0:
        return "LEFT"
    elif (c-y) < 0:
        return "RIGHT"
    if (r-x) > 0:
        return "UP"
    elif (r-x) < 0:
        return "DOWN"



def find_princess(grid):
    for index, row in enumerate(grid):
        y = row.find('p')
        if y>=0:
            return (index, y)



def main():
    n = int(input())
    r,c = [int(i) for i in input().strip().split()]
    grid = []
    for i in range(0, n):
        grid.append(input())

    print(nextMove(n,r,c,grid))


if __name__ == '__main__':
    main()
#!/usr/bin/python
#Problem: https://www.hackerrank.com/challenges/saveprincess/problem

def displayPathtoPrincess(n,grid):
    p_indexi = p_indexj = 0
    bot_indexi = bot_indexj = (n-1)/2
    if(grid[0][n-1] == 'p'):
        p_indexj = n-1
    elif(grid[n-1][0] == 'p'):
        p_indexi = n-1
    else:
        p_indexi = p_indexj = n-1

    while(bot_indexi != p_indexi):
        if(bot_indexi < p_indexi):
            print("DOWN")
            bot_indexi += 1
        else:
            print("UP")
            bot_indexi -= 1
    while(bot_indexj != p_indexj):
        if(bot_indexj < p_indexj):
            print("RIGHT")
            bot_indexj += 1
        else:
            print("LEFT")
            bot_indexj -= 1

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

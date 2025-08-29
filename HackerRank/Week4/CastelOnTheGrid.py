import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    n = len(grid)
    vis = [[False] * n for _ in range(n)]
    queue = deque([(startX, startY, 0)])
    vis[startX][startY] = True
    while queue:
        x, y, mov = queue.popleft()
        if x == goalX and y == goalY:
            return mov
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x, y
            while 0 <= nx + dx < n and 0 <= ny + dy < n and grid[nx+dx][ny+dy] == '.':
                nx += dx
                ny += dy
                if not vis[nx][ny]:
                    vis[nx][ny] = True
                    queue.append((nx, ny, mov + 1))
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()

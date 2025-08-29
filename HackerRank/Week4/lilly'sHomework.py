import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    def min_swaps(target):
        n = len(arr)
        visited = [False] * n
        index_map = {v: i for i, v in enumerate(arr)}
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i] == target[i]:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = index_map[target[j]]
                cycle_size += 1
            if cycle_size > 0:
                swaps += cycle_size - 1
        return swaps

    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]

    return min(min_swaps(sorted_arr), min_swaps(reversed_arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

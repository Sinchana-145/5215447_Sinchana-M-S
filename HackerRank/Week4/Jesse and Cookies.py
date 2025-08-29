import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, a):
    # Write your code here
    heapq.heapify(a)
    cnt = 0
    while len(a) > 1 and a[0] < k:
        x = heapq.heappop(a)
        y = heapq.heappop(a)
        heapq.heappush(a, x + 2*y)
        cnt += 1
    return cnt if a[0] >= k else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#
from collections import deque

def solve(arr, queries):
    # Write your code her
    n = len(arr)
    results = []
    for k in queries:
        dq = deque()
        maxima = []
        for i in range(n):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                maxima.append(arr[dq[0]])
        results.append(min(maxima))
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

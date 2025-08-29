import math
import os
import random
import re
import sys
def maxSubarray(arr):
    sub = arr[0]
    cur = arr[0]

    for x in arr[1:]:
        cur = max(x, cur + x)
        sub = max(sub, cur)

    seq = max(arr)
    if seq > 0:
        seq = sum(i for i in arr if i > 0)

    return [sub, seq]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

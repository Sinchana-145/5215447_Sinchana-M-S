import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    s = list(s)
    changes = [0] * n
    left, right = 0, n - 1

    while left < right:
        if s[left] != s[right]:
            if k == 0:
                return "-1"
            bigger = max(s[left], s[right])
            s[left] = s[right] = bigger
            changes[left] = changes[right] = 1
            k -= 1
        left += 1
        right -= 1

    left, right = 0, n - 1
    while left <= right and k > 0:
        if left == right:
            if k > 0 and s[left] != '9':
                s[left] = '9'
                k -= 1
        else:
            if s[left] != '9':
                if changes[left] or changes[right]:
                    if k >= 1:
                        s[left] = s[right] = '9'
                        k -= 1
                elif k >= 2:
                    s[left] = s[right] = '9'
                    k -= 2
        left += 1
        right -= 1

    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()

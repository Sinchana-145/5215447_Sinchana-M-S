import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    def primes_upto(n):
        pri = []
        num = 2
        while len(pri) < n:
            for p in pri:
                if num % p == 0:
                    break
            else:
                pri.append(num)
            num += 1
        return pri

    pri = primes_upto(q)
    abc = number
    result = []

    for i in range(q):
        prime = pri[i]
        a = []
        b = []
        while abc:
            plate = abc.pop()
            if plate % prime == 0:
                a.append(plate)
            else:
                b.append(plate)
        result.extend(reversed(a))
        abc = b

    result.extend(reversed(abc))
    return result




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

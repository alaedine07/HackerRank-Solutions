#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    lowest = scores[0]
    highest = scores[0]
    lowest_counter = 0
    heighest_counter = 0
    for score in scores:
        if score < lowest:
            lowest = score
            lowest_counter += 1
        if score > highest:
            highest = score
            heighest_counter += 1
    return [heighest_counter, lowest_counter]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    print(scores)
    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

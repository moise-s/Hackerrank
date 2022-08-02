# You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer.

# Example

# . We're working with 32 bits, so:


# Return .

# Function Description

# Complete the flippingBits function in the editor below.

# flippingBits has the following parameter(s):

# int n: an integer
# Returns

# int: the unsigned decimal integer result
# Input Format

# The first line of the input contains , the number of queries.
# Each of the next  lines contain an integer, , to process.

# Constraints


# Sample Input

# 3
# 2147483647
# 1
# 0
# Sample Output

# 2147483648
# 4294967294
# 4294967295
# Explanation

# Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get 11111111111111111111111111111110 which in turn is 4294967294.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    a = ''
    m = bin(n).replace("0b", "")
    while (len(m) < 32):
        m = '0'+m
    for i in m:
        if i == '0':
            a += '1'
        else:
            a += '0'
    return (int(a, 2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

# https://www.hackerrank.com/challenges/and-product
# Compute the bitwise & of all numbers between x and y (inclusive)

import sys


# returns the "and product" of x and y with all the bits <= diff removed
# works because the bits <= diff would be toggled while counting up from x to y
def and_product(x, y):
    diff = y - x
    diff_pow = highest_pow_2(diff)
    # mask of 0s to remove all bits needed to represent diff
    mask = pow(2, diff_pow + 1) -1
    # x & y with difference masked out
    return x & ~mask & y


# helper function to get highest power of 2 in bit representation of a number
# 2^3 = 8, so highest_pow_2(8) returns 3.  So does any number up until (not including) 16.
def highest_pow_2(num):
    if num == 0:
        return -1
    pow2 = 0
    while num > 1:
        num //= 2
        pow2 += 1
    return pow2


num_tests = int(sys.stdin.readline())
# read in each test and print the results
for test in range(num_tests):
    x, y = (int(num) for num in sys.stdin.readline().split())
    print(and_product(x,y))
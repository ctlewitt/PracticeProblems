# https://www.hackerrank.com/contests/programming-interview-questions/challenges/factorial-n
#  factorial of n on Hackerrank

import sys


def fact(n):
    if n < 0:
        return None
    ans = 1
    for num in range(1, n+1):
        ans *= num
    return ans

print(fact(int(sys.stdin.readline().strip())))
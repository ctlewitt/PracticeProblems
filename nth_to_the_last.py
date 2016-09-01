# https://www.hackerrank.com/contests/programming-interview-questions/challenges/m-th-to-last-element

import sys


def nth_to_the_last(n, lst):
    if n > len(lst):
        return "NIL"
    return lst[-n]

n = int(sys.stdin.readline().strip())
lst = sys.stdin.readline().strip().split()
print(nth_to_the_last(n, lst))

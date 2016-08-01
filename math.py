# Math: write a commandn line tool that takes an operator (+ or x) and any number of numbers, and prints out the result

import sys
from _functools import reduce
from operator import mul

_, op, *args = sys.argv
arr = map(int, args)

if op == "x":
    print("x")
    print(reduce(mul, arr, 1))
elif op == "+":
    print("+")
    print(sum(arr))
else:
    print("Bad operator; must use + or x")

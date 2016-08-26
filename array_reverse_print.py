# https://www.hackerrank.com/challenges/arrays-ds


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while len(arr) > 0:
    print(arr.pop(), end=" ")

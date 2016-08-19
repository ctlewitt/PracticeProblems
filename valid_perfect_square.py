# https://leetcode.com/problems/valid-perfect-square/
# write a function to return true if input is a square, false otherwise


def is_perfect_square(num):
    if num == 1:
        return True
    factor1 = num//2
    factor2 = 2
    while factor1 - factor2 >= 1:
        factor1 = (factor1 + factor2)//2
        factor2 = num // factor1
    if num/factor1 == factor1:
        return True
    return False


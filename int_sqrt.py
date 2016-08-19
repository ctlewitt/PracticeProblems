# https://leetcode.com/problems/valid-perfect-square/
# write a function to return true if input is a square, false otherwise


def int_sqrt(num):
    if num == 1 or num == 0:
        return num
    factor1 = num//2
    factor2 = 2
    while factor1 - factor2 >= 1:
        factor1 = (factor1 + factor2)//2
        factor2 = num // factor1
    return factor1


print(int_sqrt(0))
print(int_sqrt(4))
print(int_sqrt(9))
print(int_sqrt(16))
print(int_sqrt(25))
print(int_sqrt(36))
print(int_sqrt(49))
print(int_sqrt(1))
print(int_sqrt(3))
print(int_sqrt(7))
print(int_sqrt(15))
print(int_sqrt(24))
print(int_sqrt(35))
print(int_sqrt(48))

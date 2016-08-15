# Cracking the Coding Interview
# 8.5 Recursive Multiply: write recursive function to multiply 2 pos ints.
# minimize number of + - >> or <<
# you cannot use * or /


def mult(x, y):
    prod = 0
    bits_to_shift = 0
    shifted_y = y
    while shifted_y:
        if shifted_y & 1:
            prod += x << bits_to_shift
        bits_to_shift += 1
        shifted_y >>= 1
    return prod


def mult_rec(x, y):
    return mult_rec_aux(x, y, 0, 0)


def mult_rec_aux(x, shifted_y, bits_to_shift, prod):
    if shifted_y == 0:
        return prod
    return mult_rec_aux(x, shifted_y >> 1, bits_to_shift + 1, prod + (x << bits_to_shift) if shifted_y & 1 else prod)


print("testing iterative program")
print(mult_rec(3, 15))
print(mult (2, 3))
print(mult (0, 5))
print(mult (2, 0))
print(mult (57, 98))


print("testing recursive program")
print(mult_rec(3, 15))
print(mult_rec (2, 3))
print(mult_rec (0, 5))
print(mult_rec (2, 0))
print(mult_rec (57, 98))

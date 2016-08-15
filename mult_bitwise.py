def bitwise_multiply(x, y):
    prod = 0
    bits_to_shift = 0
    shifted_y = y
    while shifted_y:
        if shifted_y & 1:
            prod += x << bits_to_shift
        bits_to_shift += 1
        shifted_y >>= 1
    return prod

print(bitwise_multiply(2, 3))
print(bitwise_multiply(0, 5))
print(bitwise_multiply(2, 0))
print(bitwise_multiply(57, 98))
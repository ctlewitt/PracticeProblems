# write a function that, given a positive integer, returns the number of ones in the number's binary representation.
# ones(8) -> 1 (8 = 1000 in binary)
# ones(7) -> 3 (7 = 111 in binary)

def ones(num):
    num_ones = 0
    while num > 0:
        num_ones += num % 2
        num = int(num / 2)
    return num_ones

def sum_of_base_digits(num, base):
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % base
        num = int(num / base)
    return sum_of_digits

print(ones(8))
print(ones(7))

print(sum_of_base_digits(8, 2))
print(sum_of_base_digits(7, 2))
print(sum_of_base_digits(8, 8))
print(sum_of_base_digits(7, 5))



# 7
# /2 = 3 rem 1
# /2 = 1 rem 1
# /2  = 0 rem 1
#
# 8
# /2 = 4 rem 0
# /2 = 2 rem 0
# /2 = 1 rem 0
# /2 = 0 rem 1

# Therefore we want to count the number of times the number does not divide evenly by 2
#  (mainly since %2 is 0 or 1, so counting is the same as summing here)
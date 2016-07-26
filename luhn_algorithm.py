def luhn_check(cc_num):
    cc_arr = [int(digit) for digit in cc_num]
    if len(cc_arr) %2 == 0:
        start = 0
    else:
        start = 1
    for i in range(start, len(cc_arr), 2):
        cc_arr[i] *= 2
        if cc_arr[i] >= 10:
            cc_arr[i] -= 9

    return sum(cc_arr) % 10 == 0



print(luhn_check("79927398713"))
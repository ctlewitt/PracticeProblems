# https://leetcode.com/problems/valid-phone-numbers/
import re

def check_phone_numbers(filename):
    with open(filename, "r") as read_f:
        for line in read_f:
            if check_phone_number(line.strip()) is not None:
                print(line, end="")

def check_phone_number(number):
    back_number = number[-8:]
    space_or_dash = number[-9]
    front_number = number[:-9]
    if not re.fullmatch(r'^[0-9]{3}\-[0-9]{4}$', back_number):
        return None
    if space_or_dash == " ":
        return re.fullmatch(r'^\([0-9]{3}\)$', front_number)
    elif space_or_dash == "-":
        return re.fullmatch(r'^[0-9]{3}$', front_number)
    else:
        return None

check_phone_numbers("phone_numbers.txt")
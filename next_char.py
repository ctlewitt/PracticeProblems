# next char: write a function that takes a string and collects all pairs of characters (occuring sequentially) in the string;
# each pair should have a list of all characters that appear immediately after it in the string.
# Use 0 or another marker for the end of string

from collections import defaultdict
from functools import reduce

# function that fulfills description of next_char above
def next_char(my_str):
    next_char_dict = defaultdict(set)
    for char_idx in range(len(my_str) - 3): # avoid last pair of characters in string; handle null char after loop
        next_char_dict[my_str[char_idx: char_idx+2]].add(my_str[char_idx+2])
    next_char_dict[my_str[-2:]].add('\0')
    return next_char_dict

# this fulls the description of next_char above but it makes use of the more general form below
def next_char_2(my_str):
    return next_char_after_prefix_length(2, my_str)


#more general form; choose your prefix length
def next_char_after_prefix_length(prefix_len, my_str):
    next_char_dict = defaultdict(set)
    for char_idx in range(len(my_str) - (prefix_len + 1)): # avoid last pair of characters in string; handle null char after loop
        next_char_dict[my_str[char_idx: char_idx + prefix_len]].add(my_str[char_idx + prefix_len])
    next_char_dict[my_str[-prefix_len:]].add('\0')
    return next_char_dict

# get the maximum length of all of the values in a given dict
def get_max_len_val(my_dict):
    return reduce(max, map(len, my_dict.values()), 0)

print(next_char("hello"))
print(next_char("an apple and a banana"))

print(next_char_after_prefix_length(2, "hello"))
print(next_char_after_prefix_length(2, "an apple and a banana"))

print(next_char_2("hello"))
print(next_char_2("an apple and a banana"))

next_char_dict1 = next_char_after_prefix_length(1, "an apple and a banana")
next_char_dict2 = next_char_after_prefix_length(2, "an apple and a banana")
next_char_dict3 = next_char_after_prefix_length(3, "an apple and a banana")
next_char_dict4 = next_char_after_prefix_length(4, "an apple and a banana")
next_char_dict5 = next_char_after_prefix_length(5, "an apple and a banana")


# with shorter prefixes, there are some overlap between prefixes, so the number of them is fewer (len(next_char_dict))
# this quickly changes over to just being pretty close to the number of characters in the string minus the prefix length (n-k)

# with shorter prefixes, since they appear often, there are likely to be more unique character that follow each prefix string
# with longer prefixes, as these become closer and closer to unique, the number of unique characters that follow each one goes
# down to just 1.

# you can see this pattern below as each dict, unique prefixes, and max number of unique next_chars are each printed for
# different length prefixes

print(next_char_dict1)
print(len(next_char_dict1))
print(get_max_len_val(next_char_dict1))
print(next_char_dict2)
print(len(next_char_dict2))
print(get_max_len_val(next_char_dict2))
print(next_char_dict3)
print(len(next_char_dict3))
print(get_max_len_val(next_char_dict3))
print(next_char_dict4)
print(len(next_char_dict4))
print(get_max_len_val(next_char_dict4))
print(next_char_dict5)
print(len(next_char_dict5))
print(get_max_len_val(next_char_dict5))

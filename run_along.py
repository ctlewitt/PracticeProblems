# this compresses a string naively, replacing repeated characters by a single instance with the count

def run_along(my_str):
    if my_str is None or len(my_str) == 0:
        return my_str
    new_str = ""
    curr_char = my_str[0]
    curr_count = 0
    for char in my_str:
        if char == curr_char:
            curr_count += 1
        else:
            new_str = append_char_count(new_str, curr_char, curr_count)
            curr_char = char
            curr_count = 1
    new_str = append_char_count(new_str, curr_char, curr_count)
    return new_str


def append_char_count(my_str, char, count):
    return my_str + char + str(count)


print(run_along("rrreer"))
print(run_along("r"))
print(run_along("0"))
print(run_along(""))
print(run_along(None))
print(run_along("rrrrrrrrrrrr"))

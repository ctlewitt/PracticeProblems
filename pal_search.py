# palsearch: write a function that takes a string and a filename and finds a palindrome containing the substring in the
# file

def pal_search(my_str, my_file):
    file_str = ""
    with open(my_file, 'r') as read_f:
        for line in read_f:
            file_str += line.lower().strip().replace(" ", "")
    print(file_str)
    start_indices = get_substring_indices(my_str, file_str)
    for start_idx in start_indices:
        print(str(start_idx) + file_str[start_idx: start_idx + len(my_str)])


# helper to get all indicies in a string where a substring occurs
def get_substring_indices(my_substr, my_bigstr):
    next_index = -1
    start_indices = []
    found = True
    while found:
        next_index = my_bigstr.find(my_substr, next_index + 1)
        if next_index == -1:
            found = False
        else:
            start_indices.append(next_index)
    return start_indices

pal_search("test", "pal_search.txt")

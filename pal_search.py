# palsearch: write a function that takes a string and a filename and finds a palindrome containing the substring in the
# file

# note: can optimize by checking if my_str is a palindrome and if it is in file_str before doing lots of work


def pal_search(my_str, my_file):
    if my_str is None or my_str == "":
        return my_str
    file_str = ""
    with open(my_file, 'r') as read_f:
        for line in read_f:
            file_str += line.lower().strip().replace(" ", "")
    forward_start_indices = get_substring_indices(my_str, file_str)
    # reverse_indices has the exclusive(non-inclusive) indices of instances of reversed my_str
    reverse_end_indices = [idx + len(my_str) for idx in get_substring_indices(my_str[::-1], file_str)]
    for start_idx in forward_start_indices:
        for end_idx in reverse_end_indices:
            if end_idx - start_idx >= len(my_str):
                if is_palindrome(file_str[start_idx:end_idx]):
                    return file_str[start_idx:end_idx]
    return None


    # for end_idx in reverse_indices:
    #     print(str(end_idx) + file_str[end_idx - len(my_str): end_idx])
    #
    # for start_idx in forward_indices:
    #     print(str(start_idx) + file_str[start_idx: start_idx + len(my_str)])


# helper to check if a string is a palindrome
def is_palindrome(possible_palindrome):
    if possible_palindrome == "":
        return True
    if len(possible_palindrome) == 1:
        return True
    if possible_palindrome[0] != possible_palindrome[-1]:
        # first and last chars don't match
        return False
    # first and last chars match; remove and check substring
    return is_palindrome(possible_palindrome[1:len(possible_palindrome)-1])


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

print("test pal_search")
print(pal_search("test", "pal_search.txt"))
print(pal_search("ohott", "pal_search.txt"))

print()
print("test is_palindrome")
print(is_palindrome(""))
print(is_palindrome("a"))
print(is_palindrome("ab"))
print(is_palindrome("aba"))
print(is_palindrome("abba"))
print(is_palindrome("abadsfhgjhfdtrjhdfba"))
print(is_palindrome("abbasabba"))

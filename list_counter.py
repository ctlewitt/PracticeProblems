def list_counter(word):
    counts = {}
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts



print(list_counter("aabaacaba"))
print(list_counter(""))
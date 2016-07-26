# http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem

import sys

words = {"hello", "my", "name", "is", "i", "sam", "tomato", "tomatoes", "es"}
non_words = set()

def separate(my_str):
    if not my_str or my_str in words:
        return my_str
    for i in range(1, len(my_str)):
        suffix_str = my_str[i:]
        if suffix_str in words: # might need to say or if suffix_str == ""
            if my_str[:i] not in non_words:
                prefix_str = separate(my_str[:i])
                if prefix_str or prefix_str == "":
                    return prefix_str + " " + suffix_str
                #memoize:
                else:
                    non_words.add(prefix_str)


print(separate("himy"))
print(separate("hellos"))

print(separate("i"))
print(separate("hellomy"))
print(separate("hellomysam"))
print(separate("hellomyi"))
print(separate("tomato"))
print(separate("tomatoes"*2))
print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit() * 4)
print(separate("hellomynameisisamsamiistomatotomatoesestomatoesi"*200))
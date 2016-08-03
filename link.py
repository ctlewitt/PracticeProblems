# link: write a function that takes a base word and a dictionary (a set of words). Return all the words in the dictionary
# that can be made with one transformation (adding, removing, or substituting a character) to the base word.

# link("race", miriamwebster)
# -> {"ace", "brace", "rack"}

import re
import string

# this is O(nN) where n is the number of chars in word, and N is the number of elems in dictionary
# there's a better way to do this
def link(word, dictionary):
    re_words = []
    # loop through all in between (and before and after) positions
    # insert a character
    for pos in range(len(word) + 1):
        re_words.append("^" + word[:pos] + "." + word[pos:] + "$")
    # substitute or remove a character
    for pos in range(len(word)):
        re_words.append("^" + word[:pos] + ".?" + word[pos+1:] + "$")
    related_words = set()
    for re_word in re_words:
        for dict_word in dictionary:
            if re.match(re_word, dict_word) is not None:
                related_words.add(dict_word)
    return related_words


# This seems inelegant but it is actually O(n) (with a moderate constant proportional to the size of the alphabet)
# it might be more useful to talk about this in terms of O(kn) where k is the alphabet size.
# In this case, if k<N (alphabet smaller than num words in dictionary), then improved_link is faster.  Otherwise, link
# is faster.  For large dictionaries and moderate alphabets, improved_link is better.  It's interesting when you get
# into unicode because the alphabet gets larger...but so does a dictionary, typically, if it has words with non-ascii
# characters
def improved_link(word, dictionary):
    transformed_words = []
    # loop through all in between (and before and after) positions
    for pos in range(len(word) + 1):
        for char in string.ascii_letters:
            # insert a character
            transformed_words.append(word[:pos] + char + word[pos:])
    for pos in range(len(word)):
        for char in string.ascii_letters:
            # replace a character
            transformed_words.append(word[:pos] + char + word[pos+1:])
            # remove a character
            transformed_words.append(word[:pos] + word[pos+1:])
    related_words = set()
    for re_word in transformed_words:
        if re_word in dictionary:
            related_words.add(re_word)
    return related_words


print(link("aba", {"ada", "ara", "era", "ba", "a", "abba", "abbba", "abab", "bbb", "ababa"}))
print(link("", set()))
print(link("abaa", set()))

print(improved_link("aba", {"ada", "ara", "era", "ba", "a", "abba", "abbba", "abab", "bbb", "ababa"}))
print(improved_link("", set()))
print(improved_link("abaa", set()))



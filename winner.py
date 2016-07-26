import re
import string

def winner(my_str, my_list):
    my_set = set(my_list)
    max_count = 0
    max_word = ""
    broken_str = re.split(r'\W+', my_str.lower())
    word_count = {}
    for word in broken_str:
        if word in my_set:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            if word_count[word] > max_count:
                max_count = word_count[word]
                max_word = word
    print(broken_str)
    print(word_count)

    return max_word, max_count





print(winner("The Cat hello cat in hi the Hat! Rocks cat !!! Hi.", ['cat', 'hi', 'penelope jr', 'rocks']))
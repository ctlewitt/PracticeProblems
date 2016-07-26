# reverses all "words" in input string and returns modified string.
# leaves non-word characters in same position
# allows you to set the alphabet for what is a word

import re
import string

def unbreakable(my_str, alphabet):
    if len(alphabet) == 0:
        return my_str
    return re.sub(r'[' + re.escape(alphabet) + r']+', reverse, my_str)


def reverse(my_str):
    return my_str.group(0)[::-1]

print(unbreakable("helloell", "el"))

print(unbreakable("to too two", string.ascii_letters))

print(unbreakable("hello world.txt 123!", string.ascii_letters))

print(unbreakable("", string.ascii_letters))

print(unbreakable("something or other", ""))
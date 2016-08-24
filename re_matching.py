# https://leetcode.com/problems/regular-expression-matching/


def isMatch(string, regex):
    if regex == "":
        return string == ""
    if string == "":
        return lookahead(regex) == "*" and len(regex) == 2
    if regex[0] == ".":
        if lookahead(regex) == "*":
            # . occurs no times or 1 or more times
            return isMatch(string, regex[2:]) or isMatch(string[1:], regex)
        else:
            return isMatch(string[1:], regex[1:])
    else:
        if lookahead(regex) == "*":
            # first char in string occurs no times or 1 or more times
            return (string[0] == regex[0] and isMatch(string[1:], regex)) or isMatch(string, regex[2:])
        else:
            return string[0] == regex[0] and isMatch(string[1:], regex[1:])


def lookahead(regex):
    try:
        return regex[1]
    except IndexError:
        return None

print(isMatch("aa", "a"))
print(isMatch("aa", "aa"))
print(isMatch("aaa", "aa"))
print(isMatch("aa", "a*"))
print(isMatch("aa", ".*"))
print(isMatch("ab", ".*"))
print(isMatch("aab", "c*a*b"))
print(isMatch("ab", ".*c"))
print(isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))


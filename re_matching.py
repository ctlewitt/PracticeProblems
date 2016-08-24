# https://leetcode.com/problems/regular-expression-matching/


class Solution(object):
    def __init__(self):
        self.match = {}

    def isMatch(self, string, regex):
        if self.match.get((string, regex)) is not None:
            return self.match[(string, regex)]
        if regex == "":
            self.match[(string, regex)] = string == ""
            return self.match[(string, regex)]
        if string == "":
            self.match[(string, regex)] = self.lookahead(regex) == "*" and len(regex) == 2
            return self.match[(string, regex)]
        if regex[0] == ".":
            if self.lookahead(regex) == "*":
                # . occurs no times or 1 or more times
                self.match[(string, regex)] = self.isMatch(string, regex[2:]) or self.isMatch(string[1:], regex)
                return self.match[(string, regex)]
            else:
                self.match[(string, regex)] = self.isMatch(string[1:], regex[1:])
                return self.match[string, regex]
        else:
            if self.lookahead(regex) == "*":
                # first char in string occurs no times or 1 or more times
                self.match[(string, regex)] = self.isMatch(string, regex[2:]) or (string[0] == regex[0] and self.isMatch(string[1:], regex))
                return self.match[(string, regex)]
            else:
                self.match[(string, regex)] = string[0] == regex[0] and self.isMatch(string[1:], regex[1:])
                return self.match[(string, regex)]

    def lookahead(self, regex):
        try:
            return regex[1]
        except IndexError:
            return None

doer = Solution()
print(doer.isMatch("aa", "a"))
print(doer.isMatch("aa", "aa"))
print(doer.isMatch("aaa", "aa"))
print(doer.isMatch("aa", "a*"))
print(doer.isMatch("aa", ".*"))
print(doer.isMatch("ab", ".*"))
print(doer.isMatch("aab", "c*a*b"))
print(doer.isMatch("ab", ".*c"))
print(doer.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))


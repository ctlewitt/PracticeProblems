# https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, string, regex):
        if regex == "":
            return string == ""
        if string == "":
            return self.lookahead(regex) == "*" and len(regex) == 2
        if regex[0] == ".":
            if self.lookahead(regex) == "*":
                # . occurs no times or 1 or more times
                return self.isMatch(string, regex[2:]) or self.isMatch(string[1:], regex)
            else:
                return self.isMatch(string[1:], regex[1:])
        else:
            if self.lookahead(regex) == "*":
                # first char in string occurs no times or 1 or more times
                return self.isMatch(string, regex[2:]) or (string[0] == regex[0] and self.isMatch(string[1:], regex))
            else:
                return string[0] == regex[0] and self.isMatch(string[1:], regex[1:])

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


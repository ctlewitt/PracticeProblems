class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0 or len(s) == 0:
            return []
        indexes = []
        word_len = len(words[0])
        all_word_lens = word_len * len(words)
        for word_pos in range(word_len):
            start_idx = word_pos
            end_idx = word_pos + all_word_lens
            word_dict = self.fill_word_dict(s, start_idx, end_idx, word_len)
            while end_idx <= len(s) and start_idx <= len(s) - all_word_lens:
                if self.contains_all_words(words, word_dict):
                    indexes.append(start_idx)
                word_dict[s[start_idx: start_idx + word_len]] -= 1
                if s[end_idx: end_idx + word_len] in word_dict:
                    word_dict[s[end_idx: end_idx + word_len]] += 1
                else:
                    word_dict[s[end_idx: end_idx + word_len]] = 1
                start_idx += word_len
                end_idx += word_len

        return sorted(indexes)

    def fill_word_dict(self, s, start_idx, end_idx, word_len):
        word_dict = {}
        while start_idx < end_idx:
            try:
                word_dict[s[start_idx: start_idx + word_len]] += 1
            except KeyError:
                word_dict[s[start_idx: start_idx + word_len]] = 1
            start_idx += word_len
        return word_dict

    def contains_all_words(self, words, word_dict):
        copy_word_dict = dict(word_dict)
        for word in words:
            try:
                copy_word_dict[word] -= 1
            except KeyError:
                return False
        for word in words:
            if copy_word_dict.get(word) != 0:
                return False
        return True



doer = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(doer.findSubstring(s, words))

s = "barforthhihiefoobarman"
words = ["foo", "bar"]
print(doer.findSubstring(s, words))

s = "barfoothefoobarman"
words = ["foo", "bar"]
print(doer.findSubstring(s, words))

s = "toowodtoo"
words = ["wod", "too", "too"]
print(doer.findSubstring(s, words))

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(doer.findSubstring(s, words))


s = "goodgoodbestword"
words = ["word","good","best","good"]
print(doer.findSubstring(s, words))


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if "" in strs:
            return ""
        first_letter = strs[0][0]
        cut_words = []
        for word in strs:
            if word[0] != first_letter:
                return ""
            if len(word) > 1:
                cut_words += [word[1:]]
            else:
                cut_words += [""]
        return first_letter + self.longestCommonPrefix(cut_words)
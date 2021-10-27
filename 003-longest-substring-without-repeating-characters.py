class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best_length = 0
        for i in range(len(s)):
            current_substring = s[i]
            current_length = 1
            for j in range(i+1, len(s)):
                if s[j] not in current_substring:
                    current_substring += s[j]
                    current_length += 1
                else:
                    break
            if current_length > best_length:
                best_length = current_length
        return best_length
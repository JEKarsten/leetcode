class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        num_words = len(strs)
        sorted_chars = [[[], w] for w in range(num_words)]
        for w in range(num_words):
            sorted_chars[w][0] = sorted(strs[w])
        sorted_chars.sort()
        print(sorted_chars)
        result = [[strs[sorted_chars[0][1]]]]
        for w in range(1, num_words):
            if sorted_chars[w][0] == sorted_chars[w - 1][0]:
                result[-1].append(strs[sorted_chars[w][1]])
            else:
                result.append([strs[sorted_chars[w][1]]])
        return result
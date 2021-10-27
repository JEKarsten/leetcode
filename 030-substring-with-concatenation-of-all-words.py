class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        
        word_length = len(words[0])
        substring_length = word_length * len(words)
        word_map = {}
        for w in words:
            if w in word_map: word_map[w] += 1
            else: word_map[w] = 1
        
        for i in range(len(s) - substring_length + 1):
            instance_map = {}
            for j in range(len(words)):
                start_index = i + j*word_length
                current_word = s[start_index:start_index + word_length]
                if current_word in instance_map: instance_map[current_word] += 1
                else: instance_map[current_word] = 1
            if instance_map == word_map:
                result.append(i)
        
        return result
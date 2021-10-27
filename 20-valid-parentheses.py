class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return True
        if len(s) == 1: return False
        
        for i in range(len(s) - 1):
            pair = s[i:i + 2]
            if pair == "()" or pair == "[]" or pair == "{}":
                return self.isValid(s[:i] + s[i+2:])
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        return self.say(self.countAndSay(n - 1))
        
    def say(self, s):
        if s == "1": return "11"
        output = ""
        current = s[0]
        current_num = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_num += 1
            else:
                output += str(current_num) + current
                current = s[i]
                current_num = 1
            if i == len(s) - 1:
                output += str(current_num) + current
        return output
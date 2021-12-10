class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        eIndex = s.find("e")
        if eIndex == -1:
            eIndex = s.find("E")
        
        if eIndex == -1:
            s = self.remPM(s)
            return self.isDecOrInt(s)
        
        if eIndex == len(s) - 1: return False
        s1 = self.remPM(s[:eIndex])
        s2 = self.remPM(s[eIndex + 1:])
        return self.isDecOrInt(s1) and self.isInt(s2, False)
    
    def remPM(self, s):
        if not len(s): return s
        if s[0] == "+" or s[0] == "-":
            return s[1:]
        return s
        
    def isDecOrInt(self, s):
        return self.isDecimal(s) or self.isInt(s, False)
    
    def isDecimal(self, s):
        dotIndex = s.find(".")
        if dotIndex == -1: return False
        
        s1 = s[:dotIndex]
        s2 = s[dotIndex + 1:]
        if not len(s1) and not len(s2): return False
        return self.isInt(s1, True) and self.isInt(s2, True)
    
    def isInt(self, s, notEmpty):
        if not len(s):
            if notEmpty: return True
            return False
        if s[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return self.isInt(s[1:], True)
        
        return False
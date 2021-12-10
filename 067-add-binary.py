class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.helper(a, b, "")
    
    def helper(self, a, b, c):
        if not a and not b and not c: return ""
        digits = [0, 0, 0]
        if a: digits[0] = int(a[-1])
        if b: digits[1] = int(b[-1])
        if c: digits[2] = int(c)
        
        s = sum(digits)
        carry = ""
        if s > 1: carry = "1"
        lsb = "0"
        if s%2: lsb = "1"
        return self.helper(a[:-1], b[:-1], carry) + lsb
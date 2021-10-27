class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        pointer = 0
        length = len(s)
        resultS = ""
        negative = False
        
        while s[pointer] == " ":
            pointer += 1
            if pointer == length: return 0
        if s[pointer] == "+":
            pointer +=1
        elif s[pointer] == "-":
            negative = True
            pointer += 1
        if pointer == length: return 0
        
        digits = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        
        for i in range(length - pointer):
            if s[pointer + i] in ["0","1","2","3","4","5","6","7","8","9"]:
                resultS += s[pointer + i]
            else: break
        
        result = 0
        for j in range(len(resultS)):
            digit = digits[resultS[j]]
            result += digit * 10**(len(resultS) - j - 1)
        if negative: result *= -1
        return min(max(result, -2**31), 2**31 - 1)
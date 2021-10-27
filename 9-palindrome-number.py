class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstring = str(x)
        for i in range(len(xstring) // 2):
            if xstring[i] != xstring[len(xstring) - 1 - i]:
                return False
        return True
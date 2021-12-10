class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        digits = [i + 1 for i in range(n)]
        return self.helper(n, k, digits)
        
    def helper(self, n, k, digits):
        if n == 0: return ""
        block_size = factorial(n - 1)
        block = k // block_size
        if not k % block_size: block -= 1
        new_k = k - block * block_size
        return str(digits.pop(block)) + self.helper(n - 1, new_k, digits)
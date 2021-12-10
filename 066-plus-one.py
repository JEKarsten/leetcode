class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits or digits == [0]: return [1]
        if digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]
        return digits[:-1] + [digits[-1] + 1]
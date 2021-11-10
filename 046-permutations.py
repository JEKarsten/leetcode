class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        return self.helper(nums, len(nums))
    
    def helper(self, nums, layer):
        if layer == 1:
            result = []
            for n in nums:
                result += [[n]]
            return result
        
        ends = self.helper(nums, layer - 1)
        result = []
        for i in nums:
            for j in ends:
                if i not in j:
                    result += [[i] + j]
        
        return result
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running_sum = nums[0]
        max_sum = running_sum
        
        for i in range(1, len(nums)):
            running_sum = max(running_sum + nums[i], nums[i])
            max_sum = max(max_sum, running_sum)
        return max_sum
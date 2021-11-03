class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] < 1: nums.pop(i)
            else: i += 1
        nums = [0] + nums
        for i in range(len(nums)):
            current = abs(nums[i])
            if current < len(nums): nums[current] = -abs(nums[current])
        for i in range(1, len(nums)):
            if nums[i] > 0: return i
        return len(nums)
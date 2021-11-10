class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(nums))]
        
        for i in reversed(range(len(nums) - 1)):
            best_so_far = len(nums) - i - 1
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums): break
                best_so_far = min(best_so_far, 1 + dp[i + j])
            dp[i] = best_so_far
        return dp[0]
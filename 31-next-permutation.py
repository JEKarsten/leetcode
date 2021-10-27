class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return nums
        
        swap_index_l = -1
        swap_index_r = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                swap_index_l = i
                break
        if swap_index_l == -1:
            nums.reverse()
            return
        for i in reversed(range(len(nums))):
            if nums[i] > nums[swap_index_l]:
                swap_index_r = i
                break
        print(swap_index_l, swap_index_r)
        temp = nums[swap_index_l]
        nums[swap_index_l] = nums[swap_index_r]
        nums[swap_index_r] = temp
        
        for i in range(1, (len(nums) - swap_index_l)//2 + 1):
            temp = nums[swap_index_l + i]
            nums[swap_index_l + i] = nums[-i]
            nums[-i] = temp
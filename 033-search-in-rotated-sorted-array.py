class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 2:
            if nums[0] == target: return 0
            return -1
        
        start = self.find_min(nums, 0, len(nums) - 1)
        sorted_array = nums[start:] + nums[:start]
        new_spot = self.lookup(sorted_array, 0, len(nums) - 1, target)
        if new_spot == -1: return -1
        return (new_spot + start) % len(nums)
    
    def find_min(self, a, i, j):
        if i == j:
            if a[0] < a[i]: return 0
            return i
        midpoint = (i + j) // 2
        if a[midpoint] < a[0]: return self.find_min(a, i, midpoint)
        else: return self.find_min(a, midpoint + 1, j)
    
    def lookup(self, a, i, j, target):
        if i > j: return -1
        if i == j:
            if a[i] == target: return i
            else: return -1
        midpoint = (i + j) // 2
        if a[midpoint] == target: return midpoint
        elif a[midpoint] > target: return self.lookup(a, i, midpoint, target)
        else: return self.lookup(a, midpoint + 1, j, target)
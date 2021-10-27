class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4: return []
        nums.sort()
        result_set = set()
        
        for i in range(length - 3):
            w = nums[i]
            for j in range(i + 1, length - 2):
                x = nums[j]
                y_ptr = j + 1
                z_ptr = length - 1
                while y_ptr < z_ptr:
                    current_sum = w + x + nums[y_ptr] + nums[z_ptr]
                    if current_sum == target:
                        result_set.add((w, x, nums[y_ptr], nums[z_ptr]))
                        y_ptr += 1
                        while nums[y_ptr - 1] == nums[y_ptr] and y_ptr < z_ptr: y_ptr += 1
                        z_ptr -= 1
                        while nums[z_ptr] == nums[z_ptr + 1] and y_ptr < z_ptr: z_ptr -= 1
                    elif current_sum < target:
                        y_ptr += 1
                        while nums[y_ptr - 1] == nums[y_ptr] and y_ptr < z_ptr: y_ptr += 1
                    else:
                        z_ptr -= 1
                        while nums[z_ptr] == nums[z_ptr + 1] and y_ptr < z_ptr: z_ptr -= 1
        
        result = []
        for t in result_set:
            result.append(list(t))
        return list(result)
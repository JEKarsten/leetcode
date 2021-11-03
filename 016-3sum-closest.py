class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        best_diff = abs(target - result)
        for i in range(length - 1):
            x = nums[i]
            y_ptr = i + 1
            z_ptr = length - 1
            
            while y_ptr < z_ptr:
                current_sum = x + nums[y_ptr] + nums[z_ptr]
                current_diff = target - current_sum
                if abs(current_diff) < best_diff:
                    result = current_sum
                    best_diff = abs(current_diff)
                if current_diff == 0:
                    return current_sum
                elif current_diff < 0:
                    z_ptr -= 1
                    while nums[z_ptr] == nums[z_ptr + 1] and y_ptr < z_ptr: z_ptr -= 1
                else:
                    y_ptr += 1
                    while nums[y_ptr - 1] == nums[y_ptr] and y_ptr < z_ptr: y_ptr += 1
        
        return result
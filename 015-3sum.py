class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3: return []
        
        nums.sort()
        # result = []
        result = set()
        
        for i in range(length - 2):
            x = nums[i]
            y_ptr = i + 1
            z_ptr = length - 1
            
            while y_ptr < z_ptr:
                sum = x + nums[y_ptr] + nums[z_ptr]
                if sum == 0:
                    # result.append([x, nums[y_ptr], nums[z_ptr]])
                    result.add((x, nums[y_ptr], nums[z_ptr]))
                    y_ptr += 1
                    z_ptr -= 1
                    while nums[y_ptr] == nums[y_ptr - 1] and y_ptr < z_ptr: y_ptr += 1
                    while nums[z_ptr] == nums[z_ptr + 1] and y_ptr < z_ptr: z_ptr -= 1
                elif sum < 0:
                    y_ptr += 1
                    while nums[y_ptr] == nums[y_ptr - 1] and y_ptr < z_ptr: y_ptr += 1
                else:
                    z_ptr -= 1
                    while nums[z_ptr] == nums[z_ptr + 1] and y_ptr < z_ptr: z_ptr -= 1
        
        result_list = []
        for t in result:
            result_list.append(list(t))
        return result_list
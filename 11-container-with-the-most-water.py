class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pointer_l = 0
        pointer_r = len(height) - 1
        best_area = 0

        while pointer_l < pointer_r:
            current_area = (pointer_r - pointer_l) * min(height[pointer_l], height[pointer_r])
            best_area = max(current_area, best_area)
            
            if height[pointer_l] < height[pointer_r]:
                pointer_l += 1
            else:
                pointer_r -= 1
            
        return best_area
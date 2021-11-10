class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        initial_vol = 0
        peak_index = 0
        for i in range(len(height)):
            initial_vol += height[i]
            if height[i] > height[peak_index]: peak_index = i
        
        new_vol = height[peak_index]
        left = 0
        left_height = 0
        while left < peak_index:
            if height[left] > left_height:
                new_vol += (height[left] - left_height) * (peak_index - left)
                left_height = height[left]
            left += 1
        right = len(height) - 1
        right_height = 0
        while right > peak_index:
            if height[right] > right_height:
                new_vol += (height[right] - right_height) * (right - peak_index)
                right_height = height[right]
            right -= 1
        
        return new_vol - initial_vol
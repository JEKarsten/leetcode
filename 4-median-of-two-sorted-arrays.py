class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1pointer = 0
        nums2pointer = 0
        nums1len = len(nums1)
        nums2len = len(nums2)
        merged_list = []
        
        for i in range(nums1len + nums2len):
            if nums1len - nums1pointer == 0:
                merged_list += nums2[nums2pointer:]
                break
            elif nums2len - nums2pointer == 0:
                merged_list += nums1[nums1pointer:]
                break
            elif nums1[nums1pointer] < nums2[nums2pointer]:
                merged_list += [nums1[nums1pointer]]
                nums1pointer += 1
            else:
                merged_list += [nums2[nums2pointer]]
                nums2pointer += 1
        
        midway = len(merged_list) // 2
        if len(merged_list) % 2 == 1:
            return merged_list[midway]
        return (merged_list[midway - 1] + merged_list[midway]) / 2.0
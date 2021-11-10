class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[nums[0]]]
        for n in range(1, len(nums)):
            for l in range(len(result)):
                for k in range(n + 1):
                    result.append(result[0][k:] + [nums[n]] + result[0][:k])
                result.pop(0)
        final = []
        final_set = set()
        for i in result:
            final_set.add(tuple(i))
        for i in final_set:
            final.append(list(i))
        return final
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        reachable = [False for _ in range(length)]
        reachable[0] = True
        unreached = [i for i in range(length)]
        
        for i in range(length):
            if reachable[i] == False: continue
            while len(unreached) > 0:
                if unreached[0] - nums[i] - i > 0:
                    break
                else:
                    index = unreached.pop(0)
                    reachable[index] = True
        return reachable[length - 1]
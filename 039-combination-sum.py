class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        # Get rid of nums that are too small/too large
        lower_limit = target / 150
        for i in range(len(candidates)):
            if candidates[i] < lower_limit: candidates.pop(i)
            else: break
        for i in reversed(range(len(candidates))):
            if candidates[i] > target: candidates.pop(i)
            else: break
        
        dp = [[] for i in range(target + 1)]
        
        dp[0] = []
        
        for i in range(1, target + 1):
            if i in candidates: dp[i] = [[i]]
            for j in range(i):
                for k in dp[j]:
                    if i - sum(k) in candidates:
                        dp[i] += [k + [i - sum(k)]]
        
        result = []
        
        for i in range(len(dp[target])):
            solution = dp[target][i]
            solution.sort()
            if solution not in result: result += [solution]
        
        
        return result
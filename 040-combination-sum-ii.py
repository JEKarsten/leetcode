class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        
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
            candidate_list = copy.deepcopy(candidates)
            valid = True
            solution = dp[target][i]
            solution.sort()
            for j in solution:
                if j not in candidate_list:
                    valid = False
                    break
                candidate_list.remove(j)
            if valid and solution not in result: result += [solution]
        
        
        return result
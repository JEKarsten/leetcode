class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        dp = [[False for c in range(len(s) + 1)] for r in range(len(p) + 1)]
        dp[0][0] = True
        for r in range(len(p)):
            if p[r] == "*": dp[r + 1][0] = dp[r][0]
        
        for r in range(len(p)):
            for c in range(len(s)):
                match = False
                star = False

                if s[c] == p[r] or p[r] == "?":
                    match = dp[r][c]
                if p[r] == "*":
                    useIt = dp[r + 1][c]
                    loseIt = dp[r][c + 1]
                    star = useIt or loseIt
                dp[r + 1][c + 1] = star or match
            
        return dp[len(p)][len(s)]
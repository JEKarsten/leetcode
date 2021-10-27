class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2: return 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(dp)):
            if s[i] == ")":
                if s[i - 1] == ")":
                    prev = dp[i-1]
                    if i > prev and s[i - prev - 1] == "(":
                        dp[i] = prev + 2
                        if i - prev - 1 > 0:
                            dp[i] += dp[i - prev - 2]
                else:
                    dp[i] = 2
                    if i > 1:
                        dp[i] += dp[i-2]
        return max(dp)
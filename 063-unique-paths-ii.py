class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]: return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = 1
        for c in range(1, n):
            if not obstacleGrid[0][c]:
                dp[0][c] = dp[0][c - 1]
        for r in range(1, m):
            if not obstacleGrid[r][0]:
                dp[r][0] = dp[r - 1][0]
        
        for r in range(1, m):
            for c in range(1, n):
                if not obstacleGrid[r][c]:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]
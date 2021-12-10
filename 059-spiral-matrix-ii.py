class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[None for _ in range(n)] for _ in range(n)]
        val = 1
        i = 0
        j = 0
        direction = "r"
        
        for _ in range(n**2):
            matrix[i][j] = val
            
            if direction == "r":
                if j == n - 1 or matrix[i][j + 1] != None:
                    direction = "d"
                    i += 1
                else: j += 1
            elif direction == "l":
                if j == 0 or matrix[i][j - 1] != None:
                    direction = "u"
                    i -= 1
                else: j -= 1
            elif direction == "d":
                if i == n - 1 or matrix[i + 1][j] != None:
                    direction = "l"
                    j -= 1
                else: i += 1
            else:
                if i == 0 or matrix[i - 1][j] != None:
                    direction = "r"
                    j += 1
                else: i -= 1
            
            val += 1
        
        return matrix
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        num_cells = m*n
        output = []
        
        direction = "r"
        i = 0
        j = 0
        counter = 0
        
        for _ in range(m*n):
            output.append(matrix[i][j])
            matrix[i][j] = None
            counter += 1
            
            if direction == "r":
                if counter == num_cells: return output
                if j + 1 == n or matrix[i][j + 1] == None:
                    i += 1
                    direction = "d"
                    continue
                else:
                    j += 1
                    continue
            
            if direction == "l":
                if j == 0 or matrix[i][j - 1] == None:
                    i -= 1
                    direction = "u"
                    continue
                else:
                    j -= 1
                    continue
            
            if direction == "d":
                if i + 1 == m or matrix[i + 1][j] == None:
                    j -= 1
                    direction = "l"
                    continue
                else:
                    i += 1
                    continue
            
            if direction == "u":
                if i == 0 or matrix[i - 1][j] == None:
                    j += 1
                    direction = "r"
                    continue
                else:
                    i -= 1
                    continue
        return output
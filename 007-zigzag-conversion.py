class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        numChars = len(s)
        array = [["" for col in range(numChars)] for row in range(numRows)]
        currentRow = 0
        currentCol = 0
        direction = "d"
        counter = 0
        for c in s:
            array[currentRow][currentCol] = c
            counter += 1
            if currentRow == numRows - 1:
                currentRow -= 1
                currentCol += 1
                direction = "u"
            elif currentRow == 0 and direction == "u":
                currentRow += 1
                direction = "d"
            elif direction == "u":
                currentRow -= 1
                currentCol += 1
            else:
                currentRow += 1
        returnString = ""
        for i in range(numRows):
            for j in range(numChars):
                returnString += array[i][j]
        return returnString
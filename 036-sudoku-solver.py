class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.dfs(0,0)
        
    def dfs(self, row, col):
        if col == 9:
            row += 1
            col = 0
        if row == 9: return True
        if self.board[row][col] != ".": return self.dfs(row, col + 1)
        
        for e in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if not self.isValid(row, col, e): continue
            self.board[row][col] = e
            if self.dfs(row, col + 1): return True
            self.board[row][col] = "."
        return False
    
    def isValid(self, row, col, e):
        for i in range(9):
            if self.board[row][i] == e: return False
            if self.board[i][col] == e: return False
            if self.board[3*(row / 3) + (i/3)][3*(col / 3) + (i%3)] == e: return False
        return True
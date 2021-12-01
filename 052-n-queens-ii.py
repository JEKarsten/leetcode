class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.solutions = []
        self.n = n
        board = ["."*n for r in range(n)]
        self.solve(board, 0)
        return len(self.solutions)
    
    def solve(self, board, row):
        if row == self.n:
            self.solutions.append(copy.deepcopy(board))
            return
        for col in range(self.n):
            if self.check(board, row, col):
                board[row] = "."*col + "Q" + "."*(self.n - col - 1)
                self.solve(board, row + 1)
            board[row] = "."*self.n
        return
    
    def check(self, board, r, c):
        for i in range(self.n):
            if board[i][c] == "Q": return False
            if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == "Q": return False
            if r - i >= 0 and c + i < self.n and board[r - i][c + i] == "Q": return False
            if r + i < self.n and c - i >= 0 and board[r + i][c - i] == "Q": return False
            if r + i < self.n and c + i < self.n and board[r + i][c + i] == "Q": return False
        return True
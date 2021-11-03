class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        char rows[9][9];
        char columns[9][9];
        char squares[9][9];
        
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                char elem = board[row][col];
                rows[row][col] = elem;
                columns[col][row] = elem;
                squares[3 * (row / 3) + col / 3][3 * (row % 3) + col % 3] = elem;
            }
        }
        return checkArray(rows) && checkArray(columns) && checkArray(squares);
    }

private:
    bool checkArray(char (& arr)[9][9]) {
        for (int i = 0; i < 9; i++) {
            sort(arr[i], arr[i]+9);
            for (int j = 1; j < 9; j++) {
                if (arr[i][j] != '.' && arr[i][j] == arr[i][j - 1]) return false;
            }
        }
        return true;
    }
};
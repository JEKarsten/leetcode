class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n/2; col++) {
                int temp = matrix[row][col];
                matrix[row][col] = matrix[row][n - 1 - col];
                matrix[row][n - 1 - col] = temp;
            }
        }
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n - 1 - row; col++) {
                int temp = matrix[row][col];
                matrix[row][col] = matrix[n - 1 - col][n - 1 - row];
                matrix[n - 1 - col][n - 1 - row] = temp;
            }
        }
    }
}
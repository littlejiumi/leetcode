class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        int i = matrix.length - 1, j = 0;  //从左下角开始，不能右上角，因为matrix[0]有可能为空，不能得到length
        while(i>=0 && j < matrix[0].length){
            if (matrix[i][j] > target){i--;}
            else if (matrix[i][j] < target){j++;}
            else return true;
        }
        return false;
    }
}

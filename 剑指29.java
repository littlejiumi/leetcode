class Solution {
    public int[] spiralOrder(int[][] matrix) {
        if(matrix.length == 0) return new int[0];
        int left = 0, right = matrix[0].length-1, top = 0, bottom = matrix.length-1, index = 0;
        int[] result = new int[(right+1) * (bottom+1)];
        while(true){
            for(int i = left; i <= right; i++) result[index++] = matrix[top][i];
            if(++top > bottom) break;
            for(int i = top; i <= bottom; i++) result[index++] = matrix[i][right];
            if(--right < left) break;
            for(int i = right; i >= left; i--) result[index++] = matrix[bottom][i];
            if(--bottom < top) break;
            for(int i = bottom; i >= top; i--) result[index++] = matrix[i][left];
            if(++left > right) break;
        }
        return result;
    }
}

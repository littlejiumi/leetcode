class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int left = 0, right = matrix[0].length, top = 0, blow = matrix.length;
        List<Integer> res = new ArrayList<>();
        while (true){
            for (int i = left; i < right; i++){//第一行从左向右
                res.add(matrix[top][i]);
            }
            top++; //上边界收缩，判断是否结束
            if (top == blow) return res;

            for (int i = top; i < blow; i++){//最后一列从上至下
                res.add(matrix[i][right - 1]);
            }
            right--;//右边界收缩，判断是否结束
            if (right == left) return res;

            for (int i = right - 1; i >= left; i--){//最后一行从右至左
                res.add(matrix[blow - 1][i]);
            }
            blow--;//下边界收缩，判断是否结束
            if (blow == top) return res;

            for (int i = blow - 1; i >= top; i--){//第一列从下至上
                res.add(matrix[i][left]);
            }
            left++;//左边界收缩，判断是否结束
            if (left == right) return res;
        }
    }
}

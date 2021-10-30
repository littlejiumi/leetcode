class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int t = 0, b = matrix.length-1, l = 0, r = matrix[0].length-1;
        List<Integer> res = new ArrayList<>();
        while(true){ // 每一行/列都包括最后一个数写
            for(int i = l; i <= r; i++) {
                res.add(matrix[t][i]);
            }
            if(t == b) return res;  // 先比较是否合上了
            t++;                    // 再变化
            for(int i = t; i <= b; i++) {
                res.add(matrix[i][r]);
            }
            if(r == l) return res;
            r--;
            for(int i = r; i >= l; i--) {
                res.add(matrix[b][i]);
            }
            if(t == b) return res;
            b--;
            for(int i = b; i >= t; i--) {
                res.add(matrix[i][l]);
            }
            if(r == l) return res;
            l++;
        }
    }
}

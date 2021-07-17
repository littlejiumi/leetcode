class Solution {
    int m, n;
    boolean[][] visited;
    public int movingCount(int m, int n, int k) {
        this.m = m;
        this.n = n;
        visited = new boolean[m][n];
        return dfs(0, 0, k);
    }

    private int dfs(int i, int j, int k){
        if(i>=m || j >= n || visited[i][j] == true || sumNum(i) + sumNum(j) > k){
            return 0;
        }
        visited[i][j] = true;
        return 1 + dfs(i+1, j, k) + dfs(i, j+1, k);
    }

    private int sumNum(int num){
        int ans = 0;
        while(num != 0){
            ans += num % 10;
            num = num / 10;
        }
        return ans;
    }
}

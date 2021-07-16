class Solution {
    // 棋盘的行列
    int m, n;
    // 记录位置是否被遍历过
    boolean[][] visited;

    public int movingCount(int m, int n, int k) {
        this.m = m;
        this.n = n;
        visited = new boolean[m][n];
        return dfs(0, 0, k);
    }

    private int dfs(int i, int j, int k) {
        if (i >= m || j >= n
                || visited[i][j] == true
                || sum(i, j) > k) {
            return 0;
        }
        visited[i][j] = true;
        return 1 + dfs(i + 1, j, k)
                + dfs(i, j + 1, k);
    }

    private int sum(int i, int j) {
        int sum = 0;
        while (i != 0) {
            sum += i % 10;
            i /= 10;
        }
        while (j != 0) {
            sum += j % 10;
            j /= 10;
        }
        return sum;
    }
}

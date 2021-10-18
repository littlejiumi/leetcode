class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n+1];
        dp[2] = 1;
        for(int i = 3; i <= n; i++) {
            for(int j = 1; j <= i-1; j++){
                // 每次计算dp[i]，取最大的
                // j * (i - j) 是单纯的把整数拆分为两个数相乘，而j * dp[i - j]是拆分成两个以及两个以上的个数相乘
                dp[i] = Math.max(dp[i], Math.max(dp[i-j]*j, j * (i-j)));
            }
        }
        return dp[n];
    }
}

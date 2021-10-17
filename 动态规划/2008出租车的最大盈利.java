class Solution {
    public long maxTaxiEarnings(int n, int[][] rides) {
        long[] dp = new long[n + 1]; // dp[i]表示行驶到i时的最大盈利
        //按终点由小到大排序
        Arrays.sort(rides, (a, b) -> a[1] - b[1]);
        int index = 0;
        for (int i = 1; i <= n; i++) {
            //出租车从i-1位置走到i位置,不载人时他的最大收益等于dp[i-1]
            dp[i] = dp[i - 1];
            while (index < rides.length && rides[index][1] <= i) {
                //更新以i为终点载人情况的最大盈利
                dp[i] = Math.max(dp[i], dp[rides[index][0]] + rides[index][1] - rides[index][0] + rides[index][2]);
                index++;
            }
        }
        return dp[n];
    }
}

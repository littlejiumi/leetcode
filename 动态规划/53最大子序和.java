class Solution {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length]; // 以nums[i]结尾的最大子序和
        dp[0] = nums[0];
        int max = dp[0];
        for(int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(0, dp[i-1]) + nums[i];
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}

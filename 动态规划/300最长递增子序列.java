class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        for(int i = 0; i < dp.length; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j])
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        int res = 0;
        for(int i = 0; i < dp.length; i++) {
            res = Math.max(dp[i], res);
        }
        return res;
    }
}

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                # 位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i]) 
        return result

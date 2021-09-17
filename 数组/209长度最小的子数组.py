class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        if(n==0) return 0;
        int ans = n + 1;
        for(int i = 0; i < n; i++){
            int tmp = 0;
            for(int j = i; j < n; j++){
                tmp += nums[j];
                if(tmp >= target){
                    ans = Math.min(ans, j-i+1);
                    break;
                }
            }
        }
        return ans==n+1?0:ans;
    }
}

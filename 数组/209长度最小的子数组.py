class Solution {  //暴力
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


class Solution { //滑动窗口
    public int minSubArrayLen(int target, int[] nums) {
        int len = nums.length;
        if(len == 0) return 0;
        int l =0, r = 0, sum = 0;
        int ans = Integer.MAX_VALUE;
        while(r < len){
            sum += nums[r];
            while(sum >= target){
                ans = Math.min(ans, r - l + 1);
                sum -= nums[l];
                l++;
            }
            r++;
        }
        return ans == Integer.MAX_VALUE? 0: ans;
    }
}

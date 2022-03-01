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

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 定义一个无限大的数
        res = float("inf")
        Sum = 0 # 滑动窗口数值之和
        l = 0   # 滑动窗口起始位置 
        for r in range(len(nums)):  # r为滑动窗口终止位置
            Sum += nums[r]
            # 注意这里使用while，每次更新 l（起始位置），并不断比较子序列是否符合条件
            while Sum >= s:
                res = min(res, r-l+1) # 取子序列的长度
                Sum -= nums[l]
                l += 1  # 不断变更l（子序列的起始位置）
        return 0 if res==float("inf") else res

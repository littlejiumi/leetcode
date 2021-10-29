class Solution {
    public int trap(int[] height) {
        int n = height.length;
        // 如果高度数组是个空的，那么就直接返回 0
        if (n == 0) return 0;
        // leftMax[i] 用来保存从左往右看的时候，看到第 i 个时有的最大高度
        // rightMax[i] 同理，用来保存从右往左看，看到第 i 个的时候有的最大高度
        int[] leftMax = new int[n], rightMax = new int[n];
        // 它们初始状态都是各自的边界
        leftMax[0] = height[0];
        rightMax[n - 1] = height[n - 1];
        // 然后对数组进行更新，不断找从左往右看的时候看到的最大值，以及从右往左看时看到的最大值
        for (int i = 1; i < n; ++i) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i]);
            rightMax[n - i - 1] = Math.max(rightMax[n - i], height[n - i - 1]);
        }
        // 统计能够放的最大水量
        int ans = 0;
        for (int idx = 1; idx < n - 1; ++idx) {
            // 看看左右两边哪个是短板，根据短板高度和现有平台高度之差，
            // 就可以得到在下标为 i 时得到的水量，累加就好了
            ans += Math.min(leftMax[idx], rightMax[idx]) - height[idx];
        }
        return ans;
    }
}

class Solution {
    public int trap(int[] height) {
        int n = height.length;
        if(n == 0) return 0;
        // left[i] 用来保存从左往右看的时候，看到第 i 个时有的最大高度
        // right[i] 同理，用来保存从右往左看，看到第 i 个的时候有的最大高度
        int[] left = new int[n];
        int[] right = new int[n];
        // 它们初始状态都是各自的边界
        left[0] = height[0];
        right[n-1] = height[n-1];
        // 然后对数组进行更新，不断找从左往右看的时候看到的最大值，以及从右往左看时看到的最大值
        for(int i = 1; i < n; i++) {
            if(left[i-1] >= height[i]){
                left[i] = left[i-1];
            }else{
                left[i] = height[i];
            }
        }
        for(int i = n-2; i >=0; i--) {
            right[i] = Math.max(right[i+1], height[i]);
        }
        int res = 0;
            // 看看左右两边哪个是短板，根据短板高度和现有平台高度之差，
            // 就可以得到在下标为 i 时得到的水量，累加就好了
        for(int i = 1; i < n-1; i++) {
            res += (Math.min(right[i], left[i]) - height[i]);
        }
        return res;
    }
}

class Solution {
    public int maxSubArray(int[] nums) {
        int result = nums[0];
        for(int i = 1; i < nums.length; i++){
            nums[i] += Math.max(nums[i-1], 0);
            if(nums[i] > result){
                result = nums[i];
            }
        }
        return result;
    }
}

class Solution {
    public int search(int[] nums, int target) {
        int i = 0, j = nums.length-1;
        while(i <= j){
            int m = (i+j) / 2;
            if(nums[m] <= target) i = m + 1;
            else j = m - 1;
        }
        int right = i;
        if(j >= 0 && nums[j] != target) return 0;
        i = 0; j = nums.length-1;
        while(i <= j){
            int m = (i+j) / 2;
            if(nums[m] < target) i = m +1;
            else j = m -1;
        }
        int left = j;
        return right - left - 1;
    }
}

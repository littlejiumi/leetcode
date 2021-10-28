class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while(l <= r) {
            int mid = (l + r) / 2;
            if(nums[mid] == target) {
                return mid;
            }
            if (nums[mid] >= nums[0]){
                if(target < nums[mid] && nums[0] <= target){
                    r = mid-1;
                }else{
                    l = mid+1;
                }
            }else{
                if(nums[mid] <= target && target <= nums[r]){
                    l = mid+1;
                }else{
                     r = mid-1;
                }
            }
        }
        return -1;
    }
}

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:   # 小于等于号,左闭右闭
            m = l + (r - l)//2  
            if nums[m] > target:
                r = m - 1      # m-1
            elif nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
        return -1
        
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {    // 小于号,左闭右开
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                left = mid + 1;
            else if (nums[mid] > target)
                right = mid;   // 因为左闭右开，所以r=m
        }
        return -1;
    }
}

class Solution {
    public int removeElement(int[] nums, int val) {
        int fastIndex = 0;
        int slowIndex = 0;  
        for (fastIndex = 0; fastIndex < nums.length; fastIndex++) {
            if (nums[fastIndex] != val) {
                nums[slowIndex] = nums[fastIndex];
                slowIndex++;   // 遇到不是val的情况，快指针给慢指针赋值
            }
            // 遇到是val的情况，就不赋值了，只有快指针向前移动
        }
        return slowIndex;

    }
}

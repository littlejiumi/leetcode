class Solution {
/*
情况一：target 在数组范围的右边或者左边，例如数组{3, 4, 5}，target为2或者数组{3, 4, 5},target为6，此时应该返回{-1, -1}
情况二：target 在数组范围中，且数组中不存在target，例如数组{3,6,7},target为5，此时应该返回{-1, -1}
情况三：target 在数组范围中，且数组中存在target，例如数组{3,6,7},target为6，此时应该返回{1, 1} */
    public int getLeft(int[] nums, int target){
        int left = 0;
        int right = nums.length-1;
        int leftBorder = -2;
        while(left <= right) {
            int middle = left + (right - left) / 2;    
            if(nums[middle] >=  target){ // 寻找小于target最右侧的值，即左边界-1
                right = middle - 1;
                leftBorder = right;
            }else{
                left = middle + 1;
            }
        }
        return leftBorder;
    }
    // 计算出来的右边界是不包好target的最左值
    public int getRight(int[] nums, int target){ 
        int left = 0;
        int right = nums.length-1;
        int rightBorder = -2;
        while(left <= right) {
            int middle = left + (right - left) / 2;    
            if(nums[middle] <=  target){
                left = middle + 1;
                rightBorder = left;
            }else{
                right = middle - 1;
            }
        }
        return rightBorder;
    }
    public int[] searchRange(int[] nums, int target) {
        int leftBorder = getLeft(nums, target);
        int rightBorder = getRight(nums, target);
        if(leftBorder == -2 || rightBorder == -2) return new int[]{-1, -1};
        if(rightBorder - leftBorder > 1) return new int[]{leftBorder+1, rightBorder-1};
        return new int[]{-1,-1};

    }
}

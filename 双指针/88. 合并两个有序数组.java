class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m + n - 1;
        int l1 = m-1, l2 = n-1;
        while(l1 >= 0 && l2 >= 0){
            if(nums1[l1] >= nums2[l2]){
                nums1[i--] = nums1[l1--];
            }else{
                nums1[i--] = nums2[l2--];
            }
        }
        while(l1 >= 0){
            nums1[i--] = nums1[l1--];
        }
        while(l2 >= 0){
            nums1[i--] = nums2[l2--];
        }
        return;
    }
}

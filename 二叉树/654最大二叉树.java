/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return traversal(nums, 0, nums.length-1);
    }
    public TreeNode traversal(int[] nums, int L, int R) {
        //终止条件
        if(L > R) {
            return null;
        }
        int maxIndex = L;
        for(int i = L; i <= R; i++) {
            if(nums[i]>nums[maxIndex]){
                maxIndex = i;
            }
        }
        TreeNode root = new TreeNode(nums[maxIndex]); //中
        root.left = traversal(nums, L, maxIndex-1);   // 左
        root.right = traversal(nums, maxIndex+1, R); // 右
        return root;
    }
}

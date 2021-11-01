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
    public boolean traversal(TreeNode node, int count) {
        count -= node.val;
        if(count == 0 && node.left== null && node.right == null) return true;
        if(node.left != null) {
            if (traversal(node.left, count)) return true; 
        }
        if(node.right != null) {
            if (traversal(node.right, count)) return true;
        }
        return false;
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) return false;
        return traversal(root, targetSum);
    }
}

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
        if(count == 0 && node.left== null && node.right == null) return true;
        if (count != 0 && node.left== null && node.right == null) return false;
        if(node.left != null) {
            if (traversal(node.left, count - node.left.val)) return true; 
            //return traversal(node.left, count - node.left.val);
        }
        if(node.right != null) {
            if (traversal(node.right, count - node.right.val)) return true;
            // return traversal(node.right, count - node.right.val);
        }
        return false;
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) return false;
        return traversal(root, targetSum-root.val);
    }
}

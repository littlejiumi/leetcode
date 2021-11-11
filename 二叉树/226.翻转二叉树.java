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
    public TreeNode invertTree(TreeNode root) {
        // 终止条件
        if(root == null) return root;
        // 先序遍历（中）交换左右子树
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        // 遍历（左）
        root.left = invertTree(root.left);
        // 遍历（右）
        root.right = invertTree(root.right);
        return root;
    }
}

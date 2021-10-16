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
    public TreeNode invertTree(TreeNode root) {  // 前序遍历，遍历的过程中去翻转每一个节点的左右孩子就可以达到整体翻转的效果。
        if(root == null) return null;
        swapChildren(root);
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
    public void swapChildren(TreeNode root){
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
    }
}

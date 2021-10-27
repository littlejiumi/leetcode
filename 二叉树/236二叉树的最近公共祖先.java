/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q) return root;  
        // 后序遍历
        TreeNode left = lowestCommonAncestor(root.left, p, q);  // 在左子树找两个节点
        TreeNode right = lowestCommonAncestor(root.right, p, q);  // 在右子树找两个节点
        if(left == null) return right;  // 没找到，则在另一侧子树寻找
        if(right == null) return left;
        // left != NULL && right != NULL
        return root;   // 返回根节点
    }
}

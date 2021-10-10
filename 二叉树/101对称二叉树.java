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
    private boolean compare(TreeNode left, TreeNode right){
        // 终止条件如下
        // 首先排除空节点的情况
        if (left == null && right == null) return true;
        else if (left != null && right == null) return false;
        else if (left == null && right != null) return false;
        // 排除了空节点，再排除数值不相同的情况
        else if (left.val != right.val) return false;
      
        // 此时就是单层递归的逻辑：左右节点都不为空，且数值相同的情况
        // 此时才做递归，做下一层的判断
        boolean outside = compare(left.left, right.right);
        boolean inside = compare(left.right, right.left); //遍历方式 左子树左右中，右子树右左中
        boolean isSame = outside && inside;
        return isSame;
    }
    public boolean isSymmetric(TreeNode root) {
        if(root == null) return true;
        return compare(root.left, root.right);
    }
}

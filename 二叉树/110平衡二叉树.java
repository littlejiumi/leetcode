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
    public int getDepth(TreeNode node) {
        if (node == null) return 0;  // 终止条件
        int leftDepth = getDepth(node.left); // 左
        if(leftDepth == -1) return -1; //如果存在一棵子树不平衡，则整个二叉树一定不平衡。
        int rightDepth = getDepth(node.right); // 右
        if(rightDepth == -1) return -1; 
        int result = Math.abs(leftDepth-rightDepth)>1?-1:1+Math.max(leftDepth, rightDepth); // 如果不平衡返回-1；平衡返回高度
        return result;     
    }
    public boolean isBalanced(TreeNode root) {
        //后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。
      //如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回−1。
        return getDepth(root)>=0;
    }
}

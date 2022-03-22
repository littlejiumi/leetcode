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
        if (node == null) return 0; // 终止条件
        int leftDepth = getDepth(node.left); // 左子树
        int rightDepth = getDepth(node.right);  // 右子树
        //最小深度是从根节点到最近叶子节点的最短路径上的节点数量。注意是叶子节点。
        // 如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度。
        if (node.left == null && node.right != null) {
            return 1 + rightDepth;
        }
        // 右子树为空，左子树不为空，最小深度是 1 + 左子树的深度。 
        else if (node.left !=null && node.right == null) {
            return 1 + leftDepth;
        }
        // 如果左右子树都不为空或都为空，返回左右子树深度最小值 + 1 。
        int result = 1 + Math.min(leftDepth, rightDepth);
        return result;
    }
    public int minDepth(TreeNode root) {
        return getDepth(root);
    }
}
// 简洁版
class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        if (root.left == null && root.right != null) return minDepth(root.right)+1;
        if (root.right == null && root.left != null) return minDepth(root.left)+1;
        else{
            return 1 + Math.min(minDepth(root.left), minDepth(root.right));
        }
    }
}

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if root.left and not root.right: return self.minDepth(root.left)+1
        if root.right and not root.left: return self.minDepth(root.right)+1
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

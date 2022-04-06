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
    public int sumOfLeftLeaves(TreeNode root) {
        if(root == null) return 0;   // 终止条件
        int midValue = 0;       // 中
        if(root.left!=null && root.left.left == null && root.left.right == null){
            midValue = root.left.val;
        }
        int leftValue = sumOfLeftLeaves(root.left);  // 左
        int rightValue = sumOfLeftLeaves(root.right);  // 右
        return midValue + leftValue + rightValue;  // 返回值为所有左叶子之和
    }
}

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.sumOfLeftLeaves(root.left)
        r = self.sumOfLeftLeaves(root.right)
        mid = 0
        if root.left and not root.left.left and not root.left.right:
            mid = root.left.val
        return mid +l + r



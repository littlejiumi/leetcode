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
        if(node.left != null) {
            if (traversal(node.left, count-node.left.val)) return true; 
        }
        if(node.right != null) {
            if (traversal(node.right, count-node.right.val)) return true;
        }
        return false;
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) return false;
        return traversal(root, targetSum-root.val);
    }
}

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target):
            if not root.left and not root.right and target==0:
                return True 
            if root.left: 
                if dfs(root.left, target-root.left.val): return True
            if root.right: 
                if dfs(root.right, target -root.right.val): return True 
            return False
        if not root: return False
        return dfs(root, targetSum-root.val)

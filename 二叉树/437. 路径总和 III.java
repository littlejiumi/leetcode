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
    public int dfs(TreeNode root, int targetSum){
        if(root == null) return 0;
        int res = 0;
        targetSum -= root.val;
        if(targetSum == 0) res = 1;
        else res = 0;
        int leftres = dfs(root.left, targetSum);
        int rightres = dfs(root.right, targetSum );
        return res + leftres + rightres;
    }
    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) return 0;
        return dfs(root, targetSum) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum);
    }
}

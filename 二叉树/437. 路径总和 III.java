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
        res += dfs(root.left, targetSum);
        res += dfs(root.right, targetSum);
        return res;
    }

    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) return 0;
        int res = dfs(root, targetSum);
        res += pathSum(root.left, targetSum);
        res += pathSum(root.right, targetSum);
        return res;

    }
}

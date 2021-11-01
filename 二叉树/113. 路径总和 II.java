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
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    public void dfs(TreeNode root, int Sum){
        if(root.left == null && root.right == null && Sum == 0){
            res.add(new ArrayList<>(path));
            return;
        }
        if( root.left != null){
            path.add(root.left.val);
            dfs(root.left, Sum - root.left.val);
            path.remove(path.size()-1);
        }
        if( root.right != null){
            path.add(root.right.val);
            dfs(root.right, Sum-root.right.val);
            path.remove(path.size()-1);
        }
        return;
    }
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) return res;
        path.add(root.val);
        dfs(root, targetSum-root.val);
        return res;
    }
}

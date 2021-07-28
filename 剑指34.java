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
    LinkedList<List<Integer>> result = new LinkedList<>();
    LinkedList<Integer> path = new LinkedList<>();
    public List<List<Integer>> pathSum(TreeNode root, int target) {
        recur(root, target);
        return result;
    }
    void recur(TreeNode root, int target){
        if(root == null) return;
        path.add(root.val);
        target -= root.val;
        if(target == 0 && root.left == null && root.right == null){
            result.add(new LinkedList(path));
        }
        recur(root.left, target);
        recur(root.right, target);
        path.removeLast();
    }
}

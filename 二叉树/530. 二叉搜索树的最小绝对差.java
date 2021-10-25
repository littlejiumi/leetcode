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
    List<Integer> inList = new ArrayList<>();
    public void inorder(TreeNode root){
        if(root == null) return;
        inorder(root.left);
        inList.add(root.val);
        inorder(root.right);
    }
    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        int minNode = Math.abs(inList.get(0) - inList.get(1));
        for(int i = 2; i < inList.size(); i++) {
            if(Math.abs(inList.get(i)- inList.get(i-1)) < minNode){
                minNode = Math.abs(inList.get(i)- inList.get(i-1));
            }
        }

        return minNode;
    }
}

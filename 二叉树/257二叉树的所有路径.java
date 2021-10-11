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
    public void traversal(TreeNode node, List<Integer> path, List<String> result) {
        //中
        path.add(node.val);
        // 终止条件：到叶子节点
        if(node.left == null && node.right == null) {
            String pathS="";
            for (int i = 0; i < path.size()-1; i++) {
                pathS +=  path.get(i) +"->";
            }
            pathS += path.get(path.size()-1);
            result.add(pathS);
            return;
        }
        if (node.left != null) {// 左
            traversal(node.left, path, result);  
            path.remove(path.size()-1); // 回溯
        }
        if (node.right != null) { //右
            traversal(node.right, path, result);
            path.remove(path.size()-1); // 回溯
        }
    }
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>(); // 保存最终路径集合
        List<Integer> path = new ArrayList<>();  // 保存遍历路径的节点
        if(root == null) return result;
        traversal(root, path, result);
        return result;
    }
}

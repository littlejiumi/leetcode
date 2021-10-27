/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root==null || root.val == p.val || root.val == q.val){ // 没找到 或 找到了p或q
            return root;
        }
        // 后续遍历，自底向上回溯
        if (root.val > q.val && root.val > p.val){  // 往左子树遍历
            return lowestCommonAncestor(root.left, p, q);
        }else if (root.val < q.val && root.val < p.val){// 往右子树遍历
            return lowestCommonAncestor(root.right, p, q);
        }
        // 如果左右分别有p,q说明是root
        return root;
    }
}

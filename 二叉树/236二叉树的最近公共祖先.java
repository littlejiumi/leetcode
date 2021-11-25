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
        if(root == null || root == p || root == q) return root;  
        // 后序遍历
        TreeNode left = lowestCommonAncestor(root.left, p, q);  // 在左子树找两个节点
        TreeNode right = lowestCommonAncestor(root.right, p, q);  // 在右子树找两个节点
        if(left == null) return right;  // 没找到，则在另一侧子树寻找
        if(right == null) return left;
        // left != NULL && right != NULL
        return root;   // 返回根节点
    }
}

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root # 如果等于p或者q，返回
        L = self.lowestCommonAncestor(root.left, p, q)  
        R = self.lowestCommonAncestor(root.right, p, q)
        if L and R: return root  # 如果root两边分别有p和q，那就是root了，返回
        if L and not R: return L 
        if R and not L: return R 
        return None

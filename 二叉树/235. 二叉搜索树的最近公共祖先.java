/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {    // 递归法
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

public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {   // 递归法
    //如果小于等于0，说明p和q位于root的两侧，直接返回即可
    if ((root.val - p.val) * (root.val - q.val) <= 0)
        return root;
    //否则，p和q位于root的同一侧，就继续往下找
    return lowestCommonAncestor(p.val < root.val ? root.left : root.right, p, q);
}


// 迭代法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else: return root
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  #用到了二叉搜索树的中序遍历是有序数组这样的性质
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        last = res[0]
        for i in range(1, len(res)):
            if res[i] <= last:
                return False
            last = res[i]
        return True


# class Solution {
#     public boolean isValidBST(TreeNode root) {
#         return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
#     }

#     public boolean isValidBST(TreeNode node, long lower, long upper) {
#         if (node == null) {
#             return true;
#         }
#         if (node.val <= lower || node.val >= upper) {
#             return false;
#         }
#         return isValidBST(node.left, lower, node.val) && isValidBST(node.right, node.val, upper);
#     }
# }

class Solution:   # 递归法，中序遍历
    minNum = -float('inf')
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        is_left_valid = self.isValidBST(root.left)#左
        if self.minNum < root.val: self.minNum = root.val # 中： 当前最大值比root小才继续，否则返回False
        else: return False
        is_right_valid = self.isValidBST(root.right） # 右
        return is_left_valid and is_right_valid

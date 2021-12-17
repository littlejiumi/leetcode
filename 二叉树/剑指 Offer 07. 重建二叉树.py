# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dictT = dict()
        for i in range(len(inorder)):
            dictT[inorder[i]] = i
        def build(preL, preR, inL, inR): # 左右闭，四个参数分别为前序的最左最右，中序的最左最右
            # 终止条件
            if preL > preR: return
            rootVal = preorder[preL]
            # 创建根节点，每次找到根节点的val建立成root
            root = TreeNode(rootVal)
            inRoot = dictT[rootVal]
            leftLen = inRoot - inL
            # 递归生成左右子树
            root.left = build(preL+1, preL+ leftLen, inL, inRoot-1)
            root.right = build(preL+leftLen+1, preR, inRoot+1, inR)
            # 返回根节点
            return root
        return build(0, len(preorder)-1, 0, len(inorder)-1)

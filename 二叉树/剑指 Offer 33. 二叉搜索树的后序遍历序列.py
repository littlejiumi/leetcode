class Solution: #通过递归，判断所有子树的 正确性 （即其后序遍历是否满足二叉搜索树的定义）
    def verifyPostorder(self, postorder: List[int]) -> bool: # 记住二叉树的问题都用递归！关键是哪种遍历方式，这个是前序遍历，递归到i>=返回true
        def recur(i, j):
            if i >= j: return True
            middle = i
            while postorder[middle] < postorder[j]: middle += 1
            tmp = middle # 找到中点右边的那个序号
            while postorder[tmp] > postorder[j]: tmp += 1
            return tmp == j and recur(i, middle-1) and recur(middle, j-1)
        return recur(0, len(postorder) - 1)

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            middle = i
            while postorder[middle] < postorder[j]: middle += 1
            tmp = middle
            while postorder[tmp] > postorder[j]: tmp += 1
            return tmp == j and recur(i, middle-1) and recur(middle, j-1)
        return recur(0, len(postorder) - 1)

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            mid = i
            for _ in range(i, j):
                if postorder[mid] < postorder[j]: mid += 1
            temp = mid
            for _ in range(temp, j):
                if postorder[temp] > postorder[j]: temp += 1
            return temp == j and recur(i, mid-1) and recur(mid, j-1)
        return recur(0, len(postorder)-1)

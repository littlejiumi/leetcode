/*
欢迎各位勇者来到力扣城，城内设有烹饪锅供勇者制作料理，为自己恢复状态。

勇者背包内共有编号为 0 ~ 4 的五种食材，其中 materials[j] 表示第 j 种食材的数量。通过这些食材可以制作若干料理，cookbooks[i][j] 表示制作第 i 种料理需要第 j 种食材的数量，而 attribute[i] = [x,y] 表示第 i 道料理的美味度 x 和饱腹感 y。

在饱腹感不小于 limit 的情况下，请返回勇者可获得的最大美味度。如果无法满足饱腹感要求，则返回 -1。

注意：

每种料理只能制作一次。

*/

class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        ans = 0
        cookLen = len(cookbooks)
        aSum1, aSum2 = 0, 0
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        for i in range(1, cookLen+1):
            backtrack(cookLen, i, 0)
        
        for ch in res:
            flag = True
            aSum1, aSum2 = 0, 0
            temp = [0 for _ in range(5)]
            for mat in range(5):
                temp[mat] = materials[mat]
            for cook in ch:
                for mat in range(5):
                    temp[mat] -= cookbooks[cook][mat]
                    if temp[mat] < 0: 
                        flag = False
                        break
                aSum1 += attribute[cook][0]
                aSum2 += attribute[cook][1]
            if flag == True and aSum2 >= limit: 
                ans = max(ans, aSum1)
                
        return ans if ans > 0 else -1

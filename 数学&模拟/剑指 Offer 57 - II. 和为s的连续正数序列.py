class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        r = target
        res, path = [], []
        for i in range(1, r):
            s = 0
            for j in range(i, r):
                s += j
                path.append(j)
                if s == target:
                    res.append(list(path))
                elif s > target: 
                    path = []
                    break
        return res

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        l, r = [1]*len(a), [1]*len(a)
        res = []
        for i in range(1, len(a)):
            l[i] = a[i-1] * l[i-1]
        for j in range(len(a)-2, -1, -1):
            r[j] = a[j+1] * r[j+1]
        for i in range(len(a)):
            res.append(l[i]*r[i])
        return res

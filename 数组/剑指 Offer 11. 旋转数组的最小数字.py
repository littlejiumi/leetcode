class Solution:# 二分法 只能左闭右开结构
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1
        mid = (l + r) // 2
        while l < r:    # 最好采用左闭右开结构，种植条件是l==r,可以返回最后那个值
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]: l = mid + 1  # 与最右边的值比较
            elif numbers[mid] < numbers[r]: r = mid
            else: return min(numbers[l:r])
        return numbers[l]   # 返回

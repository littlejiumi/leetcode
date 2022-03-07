# 快速排序思想
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, R=-1, len(nums)
        i = 0
        while i < R:
            if nums[i]==0: # 如果等于 0， 则把 L+1 和 i 替换，并且 i+=1。这里i ++ 是因为i是从左往右遍历的，这里的拿来替换0的元素一定是1而不会出现2。
                L += 1
                nums[i], nums[L] = nums[L], nums[i]
                i+=1
                
            elif nums[i]==2: # 如果等于 2， 则把 R-1 和 i 替换，并且 i 会保持原样进行下一轮判定
                R-=1
                nums[i], nums[R] = nums[R], nums[i]
            else:
                i+=1
        
# 桶排序思想
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for i in range(len(nums)):
            if nums[i]==0:count[0]+=1
            elif nums[i]==1:count[1]+=1
            else:count[2] +=1

        i=0
        while count[0]>0:
            nums[i]=0
            count[0]-=1
            i+=1
        while count[1]>0:
            nums[i]=1
            count[1]-=1
            i+=1
        while count[2]>0:
            nums[i]=2
            count[2]-=1
            i+=1

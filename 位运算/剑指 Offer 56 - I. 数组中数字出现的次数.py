# 如果除了一个数是一个，其余都是两个，那么全部^一遍，剩下的就是那个数
# 如果如题，有两个数是一个，其余都是两个，那么全部^一遍，剩下的是那两个数
# 要把这个两个数分开，可以把整个数据集分成分别有这两个数的两部分，可以按照这两个数从最低位起不同的那一位（两数^，和0&为1）分开
# 分开之后再进行第一步就能分别剩下这两个数
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in nums:         # 1. 遍历异或
            n ^= num
        while n & m == 0:        # 2. 循环左移，计算 m
            m <<= 1       
        for num in nums:         # 3. 遍历 nums 分组
            if num & m: x ^= num # 4. 当 num & m != 0
            else: y ^= num       # 4. 当 num & m == 0
        return x, y              # 5. 返回出现一次的数字

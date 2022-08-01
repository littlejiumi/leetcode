class Solution:  # 和跳台阶问题类似，加一个判断
    def translateNum(self, num: int) -> int:
        s= str(num)
        size = len(s)
        a = b = 1
        for i in range(1, size):
            c = a + b if "10"<=s[i-1:i+1]<="25" else b
            a = b
            b = c
        return b
    
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10: return 1
        nums = str(num)
        dp = [1] * len(nums)

        dp[1] = 2 if 10 <= int(nums[:2]) < 26 else 1

        for i in range(2, len(nums)):
            dp[i] = dp[i-1] + dp[i-2] if 10<=int(nums[i-1:i+1])<26 else dp[i-1]
        return dp[len(nums)-1]


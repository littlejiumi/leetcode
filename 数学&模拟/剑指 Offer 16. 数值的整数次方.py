#快速幂法，相当于二分法，logn计算
# 参见https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0     # x为0特殊情况
        # 将n分解成2进制，带上x变成x^{bi*2^i-1}
        res = 1                 # 2^0=1，第一个数是x^{b1*2^0}
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x # 二进制为1的时候计算
            x *= x  # 每次都要计算x^{2},即x^{2^0},x^{2^1},x^{2^2}...
            n >>= 1 # 指数每次右移一位
        return res

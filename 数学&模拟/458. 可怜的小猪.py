class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 2^n个桶，可以用n只猪一次判断；3^n个桶，可以用n只猪2次判断；知道桶数，时间次数，求猪数
        return ceil(log(buckets, minutesToTest//minutesToDie + 1)) # log_{minutesToTest//minutesToDie + 1}{buckets}

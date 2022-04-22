    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            cnt, n = 0, len(nums)
            for i in range(n):
                for j in range(i, n):
                    if sum(nums[i: j+1]) == k: cnt += 1
            return cnt


    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            cnt, n = 0, len(nums)
            pre = [0] * (n + 1)
            for i in range(1, n + 1):
                pre[i] = pre[i - 1] + nums[i - 1]
            for i in range(1, n + 1):
                for j in range(i, n + 1):
                    if (pre[j] - pre[i - 1] == k): cnt += 1
            return cnt


    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            d = {}
            acc = count = 0
            for num in nums:
                acc += num
                if acc == k:
                    count += 1
                if acc - k in d:
                    count += d[acc - k]
                if acc in d:
                    d[acc] += 1
                else:
                    d[acc] = 1
            return count

public class Solution {
   public int subarraySum(int[] nums, int k) {
        int len = nums.length;
        // 计算前缀和数组
        int[] preSum = new int[len + 1];
        preSum[0] = 0;
        for (int i = 0; i < len; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }

        int count = 0;
        for (int left = 0; left < len; left++) {
            for (int right = left; right < len; right++) {
                // 区间和 [left..right]，注意下标偏移
                if (preSum[right + 1] - preSum[left] == k) {
                    count++;
                }
            }
        }
        return count;
    }
}

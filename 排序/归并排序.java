class Solution {
    int[] tmp;

    public int[] sortArray(int[] nums) {
        tmp = new int[nums.length];
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    public void mergeSort(int[] nums, int l, int r) {
        if (l >= r) {
            return;
        }
        int mid = (l + r) >> 1;
        mergeSort(nums, l, mid);
        mergeSort(nums, mid + 1, r);
        int i = l, j = mid + 1;
        int cnt = 0;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                tmp[cnt++] = nums[i++];
            } else {
                tmp[cnt++] = nums[j++];
            }
        }
        while (i <= mid) {
            tmp[cnt++] = nums[i++];
        }
        while (j <= r) {
            tmp[cnt++] = nums[j++];
        }
        for (int k = 0; k < r - l + 1; ++k) {
            nums[k + l] = tmp[k];
        }
    }
}


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, low, high):
            if low >= high:                 # 递归结束标志
                return
            mid = low + (high-low)//2       # 中间位置
            mergeSort(arr, low, mid)        # 递归对前后两部分进行排序
            mergeSort(arr, mid+1, high)
            left, right = low, mid+1        # 将arr一分为二：left指向前半部分（已有序），right指向后半部分（已有序）
            tmp = []                        # 记录排序结果
            while left <= mid and right <= high:    # 比较排序，优先添加前后两部分中的较小者
                if arr[left] <= arr[right]:         # left指示的元素较小
                    tmp.append(arr[left])
                    left += 1
                else:                               # right指示的元素较小
                    tmp.append(arr[right])
                    right += 1            
            while left <= mid:                      # 若左半部分还有剩余，将其直接添加到结果中
                tmp.append(arr[left])
                left += 1
            # tmp += arr[left:mid+1]        # 等价于以上三行
            while right <= high:                    # 若右半部分还有剩余，将其直接添加到结果中
                tmp.append(arr[right])
                right += 1
            # tmp += arr[right:high+1]      # 等价于以上三行
            arr[low: high+1] = tmp          # [low, high] 区间完成排序
        mergeSort(nums, 0, len(nums)-1)     # 调用mergeSort函数完成排序
        return nums


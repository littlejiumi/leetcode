class Solution {
    public int[] sortArray(int[] nums) {
        heapSort(nums);
        return nums;
    }

    public void heapSort(int[] nums) {
        int len = nums.length - 1;
        buildMaxHeap(nums, len);
        for (int i = len; i >= 1; --i) {
            swap(nums, i, 0);
            len -= 1;
            maxHeapify(nums, 0, len);
        }
    }

    public void buildMaxHeap(int[] nums, int len) {
        for (int i = len / 2; i >= 0; --i) {
            maxHeapify(nums, i, len);
        }
    }

    public void maxHeapify(int[] nums, int i, int len) {
        for (; (i << 1) + 1 <= len;) {
            int lson = (i << 1) + 1;
            int rson = (i << 1) + 2;
            int large;
            if (lson <= len && nums[lson] > nums[i]) {
                large = lson;
            } else {
                large = i;
            }
            if (rson <= len && nums[rson] > nums[large]) {
                large = rson;
            }
            if (large != i) {
                swap(nums, i, large);
                i = large;
            } else {
                break;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}




class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def maxHepify(arr, i, end):     # 大顶堆
            j = 2*i                     # j为i的左子节点【建堆时下标1表示堆顶】
            while j <= end:
                if j+1 <= end and arr[j+1] > arr[j]:    # i的左右子节点分别为j和j+1
                    j += 1                              # 取两者之间的较大者
                
                if arr[i] < arr[j]:             # 若i指示的元素小于其子节点中的较大者
                    arr[i], arr[j] = arr[j], arr[i]     # 交换i和j的元素，并继续往下判断
                    i = j                       # 往下走：i调整为其子节点j
                    j = 2*i                     # j调整为i的左子节点
                else:                           # 否则，结束调整
                    break
        
        n = len(nums)
        nums = [0] + nums   # nums头部添加0，满足从下标1开始建堆
        
        # 建堆【大顶堆】
        for i in range(n//2, 0, -1):    # 从第一个非叶子节点n//2开始依次往上进行建堆的调整【注意：此时堆顶为下标1】
            maxHepify(nums, i, n)
        
        # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
        for j in range(n, 0, -1):
            nums[1], nums[j] = nums[j], nums[1]     # nums[1]为堆顶元素（最大值），将其放置到尾部j
            maxHepify(nums, 1, j-1)                 # j-1变成尾部，并从堆顶1开始调整堆
        
        return nums[1:]

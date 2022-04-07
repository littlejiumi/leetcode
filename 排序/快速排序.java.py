// java
class Solution {
    public int[] sortArray(int[] nums) {
        randomizedQuicksort(nums, 0, nums.length - 1);
        return nums;
    }

    public void randomizedQuicksort(int[] nums, int l, int r) {
        if (l < r) {
            int pos = randomizedPartition(nums, l, r);
            randomizedQuicksort(nums, l, pos - 1);
            randomizedQuicksort(nums, pos + 1, r);
        }
    }

    public int randomizedPartition(int[] nums, int l, int r) {
        int i = new Random().nextInt(r - l + 1) + l; // 随机选一个作为我们的主元
        swap(nums, r, i);
        return partition(nums, l, r);
    }

    public int partition(int[] nums, int l, int r) {
        int pivot = nums[r];
        int i = l - 1;
        for (int j = l; j <= r - 1; ++j) {
            if (nums[j] <= pivot) {
                i = i + 1;
                swap(nums, i, j);
            }
        }
        swap(nums, i + 1, r);
        return i + 1;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

# Python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def randomPart(nums, L, R):
            pivot = random.randint(L, R)
            nums[pivot], nums[R] = nums[R], nums[pivot]
            i = L-1
            for j in range(L, R):
                if nums[j]<nums[R]: # 遇到比那个值小的，就换到左边，方式是设小于那个值的最右侧下标为i，交换i,j值
                    i += 1
                    nums[i],nums[j]= nums[j], nums[i]
            i+=1 # 中间值下标为i
            nums[R], nums[i] = nums[i],nums[R]
            return i

        def quickSort(nums, L, R):
            if L >= R: return
            mid = randomPart(nums, L, R)
            quickSort(nums, L, mid-1)
            quickSort(nums, mid+1, R)
        quickSort(nums, 0, len(nums)-1)
        return nums

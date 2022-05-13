public class InversionPair {

    public static void inversionPair(int[] arr) {
        if (arr == null || arr.length < 2) {
            return;
        }
        process(arr, 0, arr.length - 1);
    }

    private static void process(int[] arr, int l, int r) {
        if (l == r) {
            return;
        }
        int mid = l + ((r - l) >> 1);
        process(arr, l, mid);
        process(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }

    private static void merge(int[] arr, int l, int mid, int r) {
        int[] help = new int[r -l + 1];
        int i = 0;
        int p1 = l;
        int p2 = mid + 1;
        while (p1 <= mid && p2 <= r) {
            if (arr[p1] > arr[p2]) { //左部分有序，若其比右侧值大，则其后所有值均比右侧值大
                int temp = 0;
                while (temp < mid - p1 + 1) { //输出逆序对
                    System.out.println("(" + arr[p1 + temp] + "," + arr[p2] +")");
                    temp++;
                }
            }
            //注意此处是<=,即两数相等时取左侧数，若取右侧数，则当左部分有比右侧数大的值时，就会遗漏逆序对
            //与小和问题的此处 < 对比思考
            help[i++] = arr[p1] <= arr[p2] ? arr[p1++] : arr[p2++];
        }
        while (p1 <= mid) {
            help[i++] = arr[p1++];
        }
        while (p2 <= r) {
            help[i++] = arr[p2++];
        }
        for (i = 0; i < help.length; i++) {
            arr[l + i] = help[i];
        }
    }

    //for test
    public static void main(String[] args) {
        int[] arr = {3,2,4,3,0};
        inversionPair(arr);
    }
}


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r: return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r) # res是逆序对数量
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            k = l # 指针
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i] 
                    i += 1
                else:
                    res += m - i + 1 # 左边数组右侧的数都会比那个数大，因为有序
                    tmp[k] = nums[j]
                    j += 1
                k += 1
            while i <= m:
                tmp[k] = nums[i]
                i += 1
                k += 1
            while j <= r:
                tmp[k] = nums[j]
                j += 1
                k += 1
            nums[l : r + 1] = tmp[l:r+1]
            return res
           
        tmp = [0] * len(nums) # 归并排序空间复杂度O(n),最好，最坏，平均时间复杂度都是O(nlogn)
        return merge_sort(0, len(nums) - 1)

public class SmallSum {
    //求数组小和
    public static int smallSum(int[] arr) {
        if (arr == null || arr.length < 2) {
            return 0;
        }
        return process(arr, 0 , arr.length - 1);
    }
    //用归并排序的思想求数组小和
    private static int process(int[] arr, int l, int r) {
        if (l == r) { //只有一个元素即小和为0
            return 0;
        }
        int mid = l + ((r - l) >> 1);
        //小和等于左部分小和+右部分小和+merge过程小和
        return process(arr, l, mid) + process(arr, mid + 1, r) + merge(arr, l, mid, r);
    }
    private static int merge(int[] arr, int l, int mid, int r) {
        int[] help = new int[r - l + 1]; //辅助数组
        int i = 0;
        int p1 = l;
        int p2 = mid + 1;
        int res = 0; //小和
        while (p1 <= mid && p2 <= r) {
            //当左侧数比右侧数小时，左侧数是所有右侧数的小和需要累加的值
            res += arr[p1] < arr[p2] ? (r - p2 + 1) * arr[p1] : 0;
            //与经典merge的区别是当两数相等时取右侧数，否则会导致小和不正确
            help[i++] = arr[p1] < arr[p2] ? arr[p1++] : arr[p2++];
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
        return res;
    }

    //for test
    public static void main(String[] args) {
        int[] arr = {1,3,4,2,5};
        System.out.println(smallSum(arr));
    }
}

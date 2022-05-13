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

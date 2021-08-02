class Solution {
    public int[] getLeastNumbers(int[] arr, int k) {
        Arrays.sort(arr);
        int[] result = new int[k];
        for(int i = 0; i < k; i++) {
            result[i] = arr[i];
        }
        return result;
    }
}

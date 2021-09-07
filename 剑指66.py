class Solution {
    public int[] constructArr(int[] a) {
        int[] ans = new int[a.length];
        for (int i = 0, p = 1; i < a.length; i++) {
            ans[i] = p;
            p *= a[i];
        }
        for (int i = a.length - 1, p = 1; i >= 0; i--) {
            ans[i] *= p;
            p *= a[i];
        }
        return ans;
    }
}

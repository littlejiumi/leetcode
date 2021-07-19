class Solution {
    public int[] printNumbers(int n) {
        int maxNum = (int)Math.pow(10, n);
        int[] result = new int[maxNum-1];
        for(int i = 1; i < maxNum; i++){
            result[i-1] = i;
        }
        return result;
    }
}

class Solution {
    public String minNumber(int[] nums) {
        String[] strs = new String[nums.length];
        for(int i = 0; i < nums.length; i++) {
            strs[i] = String.valueOf(nums[i]); //int数组转换成String数组
        }
        Arrays.sort(strs, (x, y) -> (x+y).compareTo(y + x)); // lambda表达式
        StringBuilder res = new StringBuilder();
        for(String s : strs){
            res.append(s);
        }
        return res.toString();
    }
}

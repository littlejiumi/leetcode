class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> dic = new HashMap<>();
        int result = 0, tmp = 0;
        for(int j = 0; j < s.length(); j++){
            int i = dic.getOrDefault(s.charAt(j), -1);
            dic.put(s.charAt(j), j);
            tmp = tmp < j-i?tmp+1:j-i;
            result = Math.max(result, tmp);
        }
        return result;
    }
}

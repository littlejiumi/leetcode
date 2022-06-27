class Solution {
    public int characterReplacement(String s, int k) {
        int[] map = new int[26];
        int MaxLen = 0;
        int left = 0, right = 0, len = s.length();
        while(right < len){
            int r = s.charAt(right) -'A';
            map[r]++;
            MaxLen = Math.max(map[r], MaxLen);
            if(right - left + 1 > MaxLen + k){
                map[s.charAt(left)-'A']--;
                left++;
            }
            right++;
        }
        return right-left;
    }
}

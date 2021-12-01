class Solution:  # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxres = 0
        left = 0
        c_dict = {} # dict保存对儿 ch: idx
        for i in range(len(s)):
            if s[i] in c_dict:
                left = max(c_dict[s[i]]+ 1 , left)   # 如果该ch出现过，可能要缩小窗口。注意left放在当前left之后，用max
            maxres = max(maxres, i - left + 1)
            c_dict[s[i]] = i
        return maxres

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int max = 0, start = 0;
        for (int end = 0; end < s.length(); end++) {
            char ch = s.charAt(end);
            if (map.containsKey(ch)){
                start = Math.max(map.get(ch)+1,start);
            }
            max = Math.max(max,end - start + 1);
            map.put(ch,end);
        }
        return max;
    }
}

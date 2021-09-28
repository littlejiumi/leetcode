class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] cnt = new int[26];
        for (int i = 0; i < magazine.length(); i++) cnt[magazine.charAt(i) - 'a']++; //统计magazine各字符个数
        for (int i = 0; i < ransomNote.length(); i++) {
            if (--cnt[ransomNote.charAt(i) - 'a'] < 0) return false; //若消耗完小于0，说明不够用，直接返回false
        }
        return true;
    }
}

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = [0]*26
        for i in magazine:
            mag[ord(i)-ord('a')] += 1
        for i in ransomNote:
            if mag[ord(i)-ord('a')] == 0:
                return False
            mag[ord(i)-ord('a')]-=1
        return True

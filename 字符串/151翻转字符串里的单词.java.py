class Solution {
    public String reverseWords(String s) {
        // 除去开头和末尾的空白字符
        s = s.trim();
        // 正则匹配连续的空白字符作为分隔符分割
        List<String> wordList = Arrays.asList(s.split("\\s+"));
        Collections.reverse(wordList);
        return String.join(" ", wordList);
    }
}

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
  
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split(" ")
        res = " ".join(reversed(l))
        return s 
    
class Solution:
    def trim_space(self, s):
        n = len(s)
        l = 0
        r = n-1
        while l <= r and s[l]==' ': l += 1
        while l <= r and s[r]==' ': r -= 1
        tmp = []
        while l <= r:
            if s[l]!=' ':
                tmp.append(s[l])
            elif tmp[-1]!=' ':
                tmp.append(s[l])
            l += 1
        return tmp

    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right]=nums[right], nums[left]
            left += 1
            right -= 1
    def reverse_each_word(self, nums):
        l = 0
        r = 0
        n = len(nums)
        while l < n:
            while r<n and nums[r] != ' ':
                r+=1
            self.reverse_string(nums, l, r-1)
            l = r+1
            r += 1

    def reverseWords(self, s: str) -> str:
        tmp = self.trim_space(s)
        self.reverse_string(tmp, 0, len(tmp)-1)
        self.reverse_each_word(tmp)
        return "".join(tmp)

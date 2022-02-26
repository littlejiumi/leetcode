class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  isalnum() 方法检测字符串是否由字母和数字组成。
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1
        
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True

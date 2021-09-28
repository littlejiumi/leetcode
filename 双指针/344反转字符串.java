class Solution {
    public void reverseString(char[] s) {
        int l = 0;
        int r = s.length-1;
        while(l<r){
            char tmp = s[l];
            s[l]=s[r];
            s[r]=tmp;
            l++;
            r--;
        }
    }
}


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l<r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1

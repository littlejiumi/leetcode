class Solution {
    public String replaceSpace(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            if(s.charAt(i) != ' '){
                result.append(s.charAt(i));
            }else{
                result.append("%20");
            }
        }
        return result.toString();
    }
}

class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)

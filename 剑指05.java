class Solution {
    public String replaceSpace(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c==' ') sb.append("%20");
            else sb.append(c);
        }
        return sb.toString(); //返回此序列中数据的字符串表示形式
    }
}

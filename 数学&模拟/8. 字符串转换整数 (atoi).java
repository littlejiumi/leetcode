class Solution {
    public int myAtoi(String s) {
        int len = s.length();
        char[] charArray = s.toCharArray();
        int index = 0;
        while(index < len && charArray[index]==' '){
            index++;
        }
        if(index == len) return 0;
        int sign = 1;
        char firstChar = charArray[index];
        if(firstChar == '+') index++;
        else if (firstChar == '-') {
            index++;
            sign = -1;
        }
        int res = 0;
        while(index < len) {
            char c = charArray[index];
            if(c > '9' || c < '0') break;
            if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && (c - '0') > Integer.MAX_VALUE % 10)) {
                return Integer.MAX_VALUE;
            }
            if(res < Integer.MIN_VALUE / 10 || (res == Integer.MIN_VALUE / 10 && (c - '0') > -(Integer.MIN_VALUE % 10))) {
                return Integer.MIN_VALUE;
            }                
            res = (res * 10 + sign*(c-'0'));
            index++;
        }
        return res;
    }
}

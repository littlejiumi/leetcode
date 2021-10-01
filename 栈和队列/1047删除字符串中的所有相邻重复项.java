class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        int len = s.length();
        for(int i = 0;i < len; i++){
            char ch = s.charAt(i);
            if(stack.isEmpty() || stack.peek()!=ch){
                stack.push(ch);
            }else{
                stack.pop();
            }
        }
        String str = "";
        //剩余的元素即为不重复的元素
        while (!stack.isEmpty()) {
            str = stack.pop() + str;
        }
        return str;
    }
}

class Solution {
    public String removeDuplicates(String s) {
        // 将 res 当做栈
        StringBuffer res = new StringBuffer();
        // top为 res 的长度
        int top = -1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // 当 top > 0,即栈中有字符时，当前字符如果和栈中字符相等，弹出栈顶字符，同时 top--
            if (top >= 0 && res.charAt(top) == c) {
                res.deleteCharAt(top);
                top--;
            // 否则，将该字符 入栈，同时top++
            } else {
                res.append(c);
                top++;
            }
        }
        return res.toString();
    }
}

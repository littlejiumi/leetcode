class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char ch;
        for (int i = 0; i < s.length(); i++) {
            ch = s.charAt(i);
            //碰到左括号，就把相应的右括号入栈
            if (ch == '(') {
                stack.push(')');
            }else if (ch == '{') {
                stack.push('}');
            }else if (ch == '[') {
                stack.push(']');
            } else if (stack.isEmpty() || stack.peek() != ch) {
                return false;
            }else {//如果是右括号判断是否和栈顶元素匹配
                stack.pop();
            }
        }
        //最后判断栈中元素是否匹配
        return stack.isEmpty();
    }
}

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in dic: stack.append(c)
            elif len(stack)== 0 or not dic[stack.pop()] == c: return False 
        return len(stack) == 0


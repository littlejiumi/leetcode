/*成员变量

维护两个栈 stack1 和 stack2，其中 stack1 支持插入操作，stack2 支持删除操作
构造方法

初始化 stack1 和 stack2 为空
插入元素

插入元素对应方法 appendTail

stack1 直接插入元素
删除元素

删除元素对应方法 deleteHead

如果 stack2 为空，则将 stack1 里的所有元素弹出插入到 stack2 里
如果 stack2 仍为空，则返回 -1，否则从 stack2 弹出一个元素并返回
*/
class CQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    public CQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void appendTail(int value) {
        stack1.push(value);
    }
    
    public int deleteHead() {
        if (stack1.empty() && stack2.empty()){
            return -1;
        }
        if (stack2.isEmpty()){
            while(!stack1.isEmpty()){
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.appendTail(value);
 * int param_2 = obj.deleteHead();
 */

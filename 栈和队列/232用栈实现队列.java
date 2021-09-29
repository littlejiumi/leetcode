作者：落落
链接：https://zhuanlan.zhihu.com/p/100622078
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import java.util.Stack;

class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    private boolean isPushState = true;
    /** Initialize your data structure here. */
    public MyQueue() {
      // 输入栈
      stack1 = new Stack<Integer>();
      // 输出栈
      stack2 = new Stack<Integer>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
      stack1.push(x);
    }

    public void transformStack () {
        if (stack2.empty()) {
            while (!stack1.empty()) {
                int t = stack1.pop();
                stack2.push(t);
            }
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        transformStack();
        return stack2.pop();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
      return stack1.empty() && stack2.empty();
    }
}

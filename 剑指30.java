class MinStack {

    /** initialize your data structure here. **/
    Stack<Integer> stack1, stack2;
    public MinStack() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.add(x);
        if(stack2.empty() || x <= stack2.peek()) stack2.add(x);
    }
    
    public void pop() {
        if(stack1.pop().equals(stack2.peek())) stack2.pop();
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public int min() {
        return stack2.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.min();
 */

class MyStack {

    Queue<Integer> queue1; // 和栈中保持一样元素的队列
    Queue<Integer> queue2; // 辅助队列

    /** Initialize your data structure here. */
    public MyStack() {
        queue1 = new LinkedList<>();
        queue2 = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        queue2.offer(x); // 先放在辅助队列中
        while (!queue1.isEmpty()){
            queue2.offer(queue1.poll());
        }
        Queue<Integer> queueTemp;
        queueTemp = queue1;
        queue1 = queue2;
        queue2 = queueTemp; // 最后交换queue1和queue2，将元素都放到queue1中
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return queue1.poll(); // 因为queue1中的元素和栈中的保持一致，所以这个和下面两个的操作只看queue1即可
    }
    
    /** Get the top element. */
    public int top() {
        return queue1.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return queue1.isEmpty();
    }
}


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.empty(): return 
        for i in range(len(self.q1)-1):  # 剩一个就是要popleft的
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1 # 交换
        return self.q2.popleft()

    def top(self) -> int:
        if self.empty(): return 
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

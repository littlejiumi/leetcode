import queue
class MaxQueue:
    def __init__(self):
        self.deque1 = queue.deque()
        self.deque2 = queue.deque()
    def max_value(self) -> int:
        return self.deque1[0] if self.deque1 else -1
    def push_back(self, value: int) -> None:
        while self.deque1 and self.deque1[-1] < value:
            self.deque1.pop()
        self.deque1.append(value)
        self.deque2.append(value)
    def pop_front(self) -> int:
        if not self.deque1:
            return -1
        ans = self.deque2.popleft()
        if ans == self.deque1[0]:
            self.deque1.popleft()
        return ans
# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

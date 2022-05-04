class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n + 1))
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q[0]
    
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = list(range(1, n + 1))
        offset = 0
        for _ in range(n - 1):
            offset = (offset + k - 1) % len(queue)
            queue = queue[:offset] + queue[offset+1:]
        return queue[0]

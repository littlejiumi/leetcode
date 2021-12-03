"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = collections.deque()
        q.append(root)
        while q:           
            size = len(q)
            temp = []
            while size>0:
                node = q.popleft()
                temp.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                size-=1
            for i in range(len(temp)-1):
                temp[i].next = temp[i+1]
        return root




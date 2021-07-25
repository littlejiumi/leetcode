class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, idx = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]== popped[idx]:
                stack.pop()
                idx+=1
        return not stack

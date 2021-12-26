class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, idx = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[idx]:  # 注意用while，且保证stack不为空时
                stack.pop()             
                idx+=1
        return True if len(stack)==0 else False
                


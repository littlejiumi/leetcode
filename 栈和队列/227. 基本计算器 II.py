/*
对于「任何表达式」而言，我们都使用两个栈 nums 和 ops：

nums ： 存放所有的数字
ops ：存放所有的数字以外的操作
*/

class Solution:
    op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1, '^': 2}

    def calculate(self, s: str) -> int:
        s = "(" + s.replace(" ", "").replace("(-", "(0-") + ")"
        n = len(s)
        # operators & numbers
        op_stack, num_stack = [], []

        i = 0
        while i < n:
            c = s[i]
            i += 1

            if c.isdigit():  # a number 从当前位置开始继续往后取，将整一个连续数字整体取出，加入 nums
                num = int(c)
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
            elif c == '(':  # (
                op_stack.append(c)
            elif c == ')':  # calculate until see '('  使用现有的 nums 和 ops 进行计算，直到遇到左边最近的一个左括号为止，计算结果放到 nums
                while op_stack and op_stack[-1] != '(':
                    self.calc(num_stack, op_stack)
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(': 
   #  需要将操作放入 ops 中。在放入之前先把栈内可以算的都算掉（只有「栈内运算符」比「当前运算符」优先级高/同等，才进行运算），使用现有的 nums 和 ops 进行计算，直到没有操作或者遇到左括号，计算结果放到 nums
                    prev_op = op_stack[-1]
                    if self.op_priority[prev_op] < self.op_priority[c]:
                        break
                    self.calc(num_stack, op_stack)
                op_stack.append(c)

        return num_stack[0]

    def calc(self, num_stack: list, op_stack: list) -> None:
        op, y, x = op_stack.pop(), num_stack.pop(), num_stack.pop() if num_stack else 0
        ans = 0
        if op == '+':
            ans = x + y
        elif op == '-':
            ans = x - y
        elif op == '*':
            ans = x * y
        elif op == '/':
            ans = x / y
        elif op == '%':
            ans = x % y
        elif op == '^':
            ans = pow(x, y)
        num_stack.append(int(ans))

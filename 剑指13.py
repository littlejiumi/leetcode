class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j):
            # 无效情形1：机器人走出界了
            if i >= m or j >= n:
                return 0
            #无效情形2：机器人走到一个之前访问过的（因为已经访问过了，所以对于结果‘能够到达多少格子’不能再算一次了）
            if (i, j) in visited:
                return 0
            #无效情形3：数位之和>k了
            sum_i = i // 10 + i % 10 #求出i的数位和（因为题目已经限制了0<=i<=99，所以只要除数为10即可）。下同
            sum_j = j // 10 + j % 10
            if sum_i + sum_j > k: #总的数位和
                return 0

            visited.add((i, j)) #每次的有效情形都需要把坐标记录到已访问数组内
            return 1 + dfs(i+1, j) + dfs(i, j+1) 

        visited = set()
        res = dfs(0, 0)
        return res

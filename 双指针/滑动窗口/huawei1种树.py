numA = 5 #int(input())  # 共几棵树
numD = 2 #int(input())  # 死了几棵
DP = [2, 4] #list(map(int, input().split())) # 死的位置
AD = 1 #int(input())     # 补种几棵

rt = [0 for i in range(numA)]  # 种树的地方为0
for i in range(numD):
    rt[DP[i]-1] = 1  # 空的地方为1
winl = 0
winr = -1
mxt = 0
while winr < numA:
    if sum(rt[winl: winr+1]) <= AD:     # 空的地方小于补种的数量，可以一直扩大窗口
        winr += 1
    else:   # 大于补种的数量，需要左边缩小窗口
        winl += 1
    mxt = max(mxt, winr - winl)  
print(mxt)

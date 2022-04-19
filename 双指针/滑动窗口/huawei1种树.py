numA = 5 #int(input())
numD = 2 #int(input())
DP = [2, 4] #list(map(int, input().split()))
AD = 1#int(input())

rt = [0 for i in range(numA)]
for i in range(numD):
    rt[DP[i]-1] = 1
winl = 0
winr = -1
mxt = 0
while winr < numA:
    if sum(rt[winl:winr+1]) <= AD:
        winr += 1
    else:
        mxt = max(mxt, winr - winl)
        winl += 1
        mxt = max(mxt, winr - winl)
print(mxt)

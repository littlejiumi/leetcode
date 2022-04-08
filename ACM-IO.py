# 输入包括两个正整数a,b(1 <= a, b <= 1000),输入数据包括多组。
while True:
    try:
        a, b = map(int,input().split())
        print(a+b)
    except:
        break
        
        
# 输入第一行包括一个数据组数t(1 <= t <= 100)
# 接下来每行包括两个正整数a,b(1 <= a, b <= 1000)
t = int(intput())
for i in range(t):
  a, b = map(int, input().split())
  print(a+b)
  
  
# 输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入  
while True:
    try:
        a,b=map(int, input().split())
        if a == 0 and b == 0:
            break
        else:
            print(a+b)
    except:
        break
# 输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
# 接下来t行, 每行一组数据。
# 每行的第一个整数为整数的个数n(1 <= n <= 100)。
# 接下来n个正整数, 即需要求和的每个正整数。        
while True:
    try:
        a = int(input())
        for i in range(a):
            li = list(map(int, input().split()))
            print(sum(li[1:]))
    except: 
        break

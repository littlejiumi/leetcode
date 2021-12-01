class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = Counter(s1) #s1的哈希表，实质是字典
        c2 = Counter() #实例化一个counter类
        p = q = 0  #设定下标初始化为0，滑动窗口就是[p,q]
        #下面就是不断在s2上面进行滑动窗口，不断更新哈希表进行比较
        while q < l2:
            c2[s2[q]] += 1   #统计字典哈希表
            if c1 == c2:  # 每个窗口个都跟s1组成的c1做比较
                return True  #注意，这种结果性条件判断一定是写在前面
            q += 1           #s2滑动窗口，下标后移
            if q - p + 1 > l1:   #为什么有这个呢？因为第一个滑动窗口比较特殊，要先构造第一个完整的滑动窗口，后面才是更新边界
                c2[s2[p]] -= 1   #字典哈希表移除最前面的字符
                if c2[s2[p]] == 0:  #由于counter特性，如果value为0，就删除它
                #否则会出现s1的map没有a，但是s2的map的a为0，此时是成立的，但是导致了这两个map不相等，结果出错
                    del c2[s2[p]]
                p += 1     #最前面的下标右移动
        return False  #遍历所有滑动窗口过后，仍然没返回true，那就是不合题意

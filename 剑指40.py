class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
    
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]  # 需要最大堆，而python只有最小堆，故全部取负值
        heapq.heapify(hp)  # 把list变成heap，堆的大小为hp长度k
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:  #如果该数大于最大堆堆顶的值，换掉堆顶
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

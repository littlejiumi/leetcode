class Solution:
    def reversePairs(self, nums: List[int]) -> int: 
        def mergesort(nums, left, right):
            if left >= right:
                return 0
            mid = left + (right - left) // 2

            cnt_l = mergesort(nums, left, mid)
            cnt_r = mergesort(nums, mid + 1, right)
            cnt_c = merge(nums, left, mid, right)

            return cnt_l + cnt_r + cnt_c

        def merge(nums, left, mid, right):
            tmp, cnt = [], 0
            l1, l2 = left, mid + 1

            while l1 <= mid and l2 <= right:
                if nums[l1] <= nums[l2]:
                    tmp.append(nums[l1])
                    l1 += 1
                else:
                    tmp.append(nums[l2])
                    l2 += 1
                    cnt += (mid - l1 + 1)
            
            if l1 <= mid:
                tmp.extend(nums[l1 : mid + 1])
            else:
                tmp.extend(nums[l2 : right + 1])

            nums[left : right + 1] = tmp[:]
            return cnt
    
        return mergesort(nums, 0, len(nums) - 1)

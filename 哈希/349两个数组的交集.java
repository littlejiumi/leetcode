class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        if(nums1.length == 0 || nums2.length == 0){
            return new int[0];
        }
        Set<Integer> interSet = new HashSet<>();
        Set<Integer> set1 = new HashSet<>();
        for(int i : nums1){
            set1.add(i);
        }
        for(int i : nums2){
            if(set1.contains(i)){
                interSet.add(i);
            }
        }
        int[] result = new int[interSet.size()];
        int index = 0;
        for(Integer i : interSet){
            result[index++] = i;
        }
        return result;
    }
}

#python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))  # 注意set（）求交集用 & 运算符

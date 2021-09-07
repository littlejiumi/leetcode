class Solution {   //哈希表
    public int majorityElement(int[] nums) {
        int bound = nums.length / 2;
        Map<Integer, Integer> counts = new HashMap<>();
        for(int num: nums){
            if(!counts.containsKey(num)) {
                counts.put(num, 1);
            }else{
                counts.put(num, counts.get(num) + 1);
            }
            if (counts.get(num) > nums.length / 2) return num;
        }
        return 0;
    }
}

class Solution {  // 排序
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}

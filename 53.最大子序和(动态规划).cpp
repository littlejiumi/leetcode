class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int size = nums.size();
        int res = nums[0];
        int sum = 0;
        for(int i = 0; i < size;i++) {
            if(sum > 0){
                sum += nums[i];
            }else{
                sum = nums[i];  //若sum<0则肯定不要前面的了；
            }
            res = max(res, sum);  //每次都与最大值比较，取最大保留
        }
        return res;
    }
};

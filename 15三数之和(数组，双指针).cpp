class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int now;
        vector<vector<int>> ans;
        for(int i = 0; i < nums.size(); i++ ) {
            now = nums[i];
            if(now > 0 ) break;
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int l = i +1, r= nums.size() - 1;
            while(l<r) {
                if(nums[l] + nums[r] +now <0)l++;
                else if(nums[l] + nums[r] +now > 0) r--;
                else{
                    ans.push_back({now, nums[l], nums[r]});
                    l++, r--;
                    while(l<r && nums[l]==nums[l-1])l++;
                    while(l<r && nums[r] == nums[r+1])r--;
                }
            }
        }
        return ans;
    }
};

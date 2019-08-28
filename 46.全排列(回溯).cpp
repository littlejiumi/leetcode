class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size() == 0)
            return res;
        vector<int> tmp;
        helper(res, tmp, nums);
        return res;
    }
    
    void helper(vector<vector<int>> &res, vector<int> tmp, vector<int> nums) {
        if(nums.size() == tmp.size())
            res.push_back(tmp);
        else {
            for(int i = 0; i < nums.size(); i++) {
                if(count(tmp.begin(),tmp.end(),nums[i])) continue;
                tmp.push_back(nums[i]);
                helper(res, tmp, nums);
                tmp.pop_back();
            }
        }
    }
};

/*
对于回溯问题，总结出一个递归函数模板，包括以下三点

递归函数的开头写好跳出条件，满足条件才将当前结果加入总结果中
已经拿过的数不再拿 if(s.contains(num)){continue;}
遍历过当前节点后，为了回溯到上一步，要去掉已经加入到结果list中的当前节点。*/

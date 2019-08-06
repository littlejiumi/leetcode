class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0) return "";
        int len = strs.size();
        string ans = strs[0];
        for(int i = 1; i < len; i++ ) {
            int j = 0;
            for(; j < ans.length() && j < strs[i].length(); j++ ) {
                if(ans[j] != strs[i][j] ){
                    break;                  
                }                            
            }
            ans = ans.substr(0, j);
            if(ans == "") {
                return ans;
            }
        }
        return ans;
    }
};

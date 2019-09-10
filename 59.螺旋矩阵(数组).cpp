class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        if(n==0) return {{}};
        vector<vector<int> > res(n,vector<int>(n,0));
        int down=0,up=n-1,left=0,right=n-1;
        int itm=1;
        while(left<=right && down<=up){
            for(int i=left;i<=right;i++) res[down][i]=itm++;
            for(int i=down+1;i<=up;i++) res[i][right]=itm++;
            for(int i=right-1;i>=left;i--) res[up][i]=itm++;
            for(int i=up-1;i>=down+1;i--) res[i][left]=itm++;
            down++;
            up--;
            left++;
            right--;
        }
        return res;
    }
};

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n, 0));
        int c = 1, j = 0;
        while(c <= n * n) {
            for(int i = j; i < n - j; i++ ) {
                ans[j][i] = c++;
            }
            for(int i = j + 1 ; i < n - j; i++) {
                ans[i][n - j - 1] = c++;
            }
            for(int i = n - j - 2; i >= j; i--) {
                ans[n - j - 1][i] = c++;
            }
            for(int i = n - j - 2; i > j; i--) {
                ans[i][j] = c++;
            }
            j++;
        }
        return ans;
    }
};

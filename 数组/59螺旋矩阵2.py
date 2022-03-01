class Solution {
    public int[][] generateMatrix(int n) {
        int l = 0, r = n-1, t = 0, b = n-1;
        int num = 1;
        int[][] ans = new int[n][n];
        while(num <= n * n){
            for(int i = l; i <= r; i++){ans[t][i]=num++;}
            t++;
            for(int i = t; i <= b; i++){ans[i][r] = num++;}
            r--;
            for(int i = r; i >= l; i--){ans[b][i] = num++;}
            b--;
            for(int i = b; i >= t; i--){ans[i][l] = num++;}
            l++;
        }
        return ans;
    }
}

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        l, r, t, b = 0, n-1, 0, n-1
        total = n*n
        temp = 1
        while temp <= total:
            for i in range(l, r+1):  # 注意要左闭右闭，这样才能下一步t=t+1
                res[t][i] = temp 
                temp += 1
            t+=1
            for i in range(t, b+1):
                res[i][r] = temp
                temp+=1
            r -=1
            for i in range(r, l-1, -1):
                res[b][i] = temp
                temp+=1
            b -= 1
            for i in range(b,t-1,-1):
                res[i][l] = temp
                temp+=1
            l += 1
        return res

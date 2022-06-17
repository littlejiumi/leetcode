import java.util.*;


public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * longest common substring
     * @param str1 string字符串 the string
     * @param str2 string字符串 the string
     * @return string字符串
     */
    public String LCS (String str1, String str2) {
        int m = str1.length();
        int n = str2.length();
        int res= 0, start=0;
        int[][] dp = new int[m+1][n+1];
        for(int i = 1; i<=m ; i++) {
            for(int j = 1; j <= n; j++) {
                if(str1.charAt(i-1) == str2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1]+1;
                }
                if(dp[i][j] > res){
                    res = dp[i][j];
                    start = i-res;
                }
            }
        }
        return str1.substring(start, start+res);
    }
}

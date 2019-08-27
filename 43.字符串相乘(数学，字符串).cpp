class Solution {
public:
    string multiply(string num1, string num2) {
        if(num1 == "0" || num2 == "0") return "0";
        /**
        num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j, i+j+1]
        例: 123 * 45,  123的第1位 2 和45的第0位 4 乘积 08 存放在结果的第[1, 2]位中
          index:    0 1 2 3 4  
              
                        1 2 3
                    *     4 5
                    ---------
                          1 5
                        1 0
                      0 5
                    ---------
                      0 6 1 5
                        1 2
                      0 8
                    0 4
                    ---------
                    0 5 5 3 5
        这样我们就可以单独都对每一位进行相乘计算把结果存入相应的index中        
        **/
        int n1 = num1.length() - 1;
        int n2 = num2.length() - 1;
        if(n1 < 0 || n2 < 0) return "";
        vector<int> mul(n1+n2+2);
        
        for(int i = n1; i >=0; i--) {
            for(int j = n2; j >= 0; j--) {
                int bitmul = (num1[i] - '0') * (num2[j] - '0');
                bitmul += mul[i + j + 1]; //先加低位，判断是否有新的进位
                mul[i+j] += bitmul / 10;
                mul[i+j+1] = bitmul % 10;
            }
        }
        //去掉前导0
            int i = 0;
            while(i <n1 + n2 + 1 && mul[i] == 0)i++;
            string multi;
            for(;i<n1+n2+2;++i){
                multi.append(to_string(mul[i]));
            }
            return multi;
    }
};

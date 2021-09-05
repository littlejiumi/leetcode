class Solution { //无进位和 与 异或运算 规律相同，进位 和 与运算 规律相同（并需左移一位）
    public int add(int a, int b) {  // s = a + b = n + c
        while(b != 0) { // 当进位为 0 时跳出, 无需进位即计算结束
            int c = (a & b) << 1;  // c = 进位， 与运算并左移一位
            a ^= b; // a = 非进位和， 异或运算
            b = c; // b = 进位
        }
        return a;
    }
}

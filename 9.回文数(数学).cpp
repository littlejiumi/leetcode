//由于回文数的位数可奇可偶，所以当它的长度是偶数时，它对折过来应该是相等的；当它的长度是奇数时，那么它对折过来后，有一个的长度需要去掉一位数（除以 10 并取整）。
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || (x%10 == 0) && x != 0) return false;
        else if(x == 0) return true;
        else{
            int rev = 0;
            while(x > rev) {
                rev  = rev * 10 + x % 10;
                x /= 10;
            }
            return (x == rev) || (rev/10 == x);
        }
    }
};

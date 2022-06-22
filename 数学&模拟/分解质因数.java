public class Solution {
    /**
     * @param num an integer
     * @return an integer array
     */
    public List<Integer> primeFactorization(int num) {
        List<Integer> factors = new ArrayList<Integer>();
        for (int i = 2; i * i <= num; i++) {
            while (num % i == 0) {
                num = num / i;
                factors.add(i);
            }
        }
        //若最后剩余数不为1，则为最后一个质因数
        if (num != 1) {
            factors.add(num);
        }   
        return factors;
    }
}

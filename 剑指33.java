class Solution {
    public boolean verifyPostorder(int[] postorder) {
        return recur(postorder, 0, postorder.length - 1);
    }
    boolean recur(int[] postorder, int i, int j){
        if(i >= j) return true;
        int middle = i;
        while(postorder[middle] < postorder[j]) middle++;
        int tmp = middle;
        while(postorder[tmp] > postorder[j]) tmp++;
        return tmp == j && recur(postorder, i, middle-1) && recur(postorder, middle, j-1);
    }
}

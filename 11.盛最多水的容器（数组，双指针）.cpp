class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size() - 1;
        int vol = 0;
        while(i < j) {
            int minum = min(height[i], height[j]);
            int tmp = minum * (j - i);
            vol = max(tmp, vol);
            if(height[i] > height[j]){
                j--;
            }else{
                i++;
            }
        }
        return vol;
    }
};

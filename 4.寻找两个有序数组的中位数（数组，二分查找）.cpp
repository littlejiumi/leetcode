class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        
        if(n > m) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int L1max, R1min, L2max, R2min, low = 0, high = 2*n, c1, c2;
        
        while(low <= high) {
            
            c1 = (low + high) / 2;
            c2 = m + n - c1;
            
            L1max = (c1 == 0) ? INT_MIN : nums1[(c1 - 1) / 2];
            R1min = (c1 == 2 * n) ? INT_MAX : nums1[c1 / 2];
            L2max = (c2 == 0) ? INT_MIN : nums2[(c2 - 1) / 2];
            R2min = (c2 == 2 * m) ? INT_MAX : nums2[c2 / 2];
            
            if(L1max > R2min) high = c1 - 1;
            else if(L2max > R1min) low = c1 + 1;
            else break;
        }
        return (max(L1max, L2max) + min(R1min, R2min)) / 2.0;
    }
};

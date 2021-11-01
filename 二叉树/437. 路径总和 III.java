class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        if (root == NULL) return 0;
        return pathWithRoot(root, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }

    int pathWithRoot(TreeNode* root, int sum) {
        if (root == NULL) return 0;
        sum = sum - root->val;
        return (sum == 0 ? 1 : 0) + pathWithRoot(root->left, sum) + pathWithRoot(root->right, sum);
    }
};


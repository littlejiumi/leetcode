class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return buildTree1(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1);
    }
    public TreeNode buildTree1(int[] inorder, int inLeft, int inRight,
                               int[] postorder, int postLeft, int postRight) {
        // 没有元素了
        if (inRight - inLeft < 0) {
            return null;
        }
        // 后序数组postorder里最后一个即为根结点
        int rootVal = postorder[postRight];
        TreeNode root = new TreeNode(rootVal);
        int rootIndex = 0;
        // 根据根结点的值找到该值在中序数组inorder里的位置
        for (int i = inLeft; i <= inRight; i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
            }
        }
        // 根据rootIndex划分左右子树
        root.left = buildTree1(inorder, inLeft, rootIndex-1,
                postorder, postLeft, postLeft + (rootIndex - inLeft)-1);
        root.right = buildTree1(inorder, rootIndex + 1, inRight,
                postorder, postLeft + (rootIndex - inLeft), postRight - 1);
        return root;
    }
}

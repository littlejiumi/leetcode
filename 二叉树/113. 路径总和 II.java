/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    public void dfs(TreeNode root, int Sum){
        if(root.left == null && root.right == null && Sum == 0){
            res.add(new ArrayList<>(path));
            return;
        }
        if( root.left != null){
            path.add(root.left.val);
            dfs(root.left, Sum - root.left.val);
            path.remove(path.size()-1);
        }
        if( root.right != null){
            path.add(root.right.val);
            dfs(root.right, Sum-root.right.val);
            path.remove(path.size()-1);
        }
        return;
    }
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) return res;
        path.add(root.val);
        dfs(root, targetSum-root.val);
        return res;
    }
}

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, target):
            if target==0 and not root.left and not root.right:
                res.append(path[:])
                return
            if root.left!=None:
                path.append(root.left.val)
                recur(root.left, target-root.left.val)
                path.pop()
            if root.right!=None:
                path.append(root.right.val)
                recur(root.right, target-root.right.val)
                path.pop()
            return
        if not root: return None
        path.append(root.val)
        recur(root, targetSum-root.val)
        return res


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
    public int dfs(TreeNode root, int targetSum){
        if(root == null) return 0;
        int res = 0;
        targetSum -= root.val;
        if(targetSum == 0) res = 1;
        res += dfs(root.left, targetSum);
        res += dfs(root.right, targetSum);
        return res;
    }

    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) return 0;
        int res = dfs(root, targetSum);
        res += pathSum(root.left, targetSum);
        res += pathSum(root.right, targetSum);
        return res;

    }
}

// 树的遍历并同时求前缀和，遍历当前节点时计算当前值-targetSum在前缀map中是否有了
class Solution {
    int ans = 0;
    public int pathSum(TreeNode root, int targetSum) {
        // 记录路径中某个前缀和出现的次数
        Map<Integer, Integer> map = new HashMap<>();
        // 防止包含根节点的时候找不到
        map.put(0, 1);
        // 开始搜索
        dfs(root, map, 0, targetSum);
        // 返回值
        return ans;
    }

    private void dfs(TreeNode node, Map<Integer, Integer> map, int currSum, int targetSum) {
        // 递归退出条件
        if (node == null) {
            return;
        }
        // 判断是否存在符合条件的前缀和
        currSum += node.val;
        ans += map.getOrDefault(currSum - targetSum, 0);
        // 将当前前缀和记录下来
        map.put(currSum, map.getOrDefault(currSum, 0) + 1);
        // 继续往下递归
        dfs(node.left, map, currSum, targetSum);
        dfs(node.right, map, currSum, targetSum);
        // 回溯，恢复状态
        map.put(currSum, map.getOrDefault(currSum, 0) - 1);
    }
}


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
    public int findBottomLeftValue(TreeNode root) {
        List<List<Integer>> layers = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> layer = new ArrayList<>();
            while(size!=0) {
                TreeNode cur = queue.poll();
                layer.add(cur.val);
                if(cur.left != null) queue.offer(cur.left);
                if(cur.right != null) queue.offer(cur.right);
                size--;
            }
            layers.add(layer);
        }
        int size = layers.size();
        return layers.get(size-1).get(0);
    }
}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return
        queue = [root]      
        while len(queue)!=0:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i == 0: res = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
        

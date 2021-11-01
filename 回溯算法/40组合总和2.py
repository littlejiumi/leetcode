class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(candidates, target, sum, startIndex):
            if sum > target: return
            if sum == target:
                res.append(path[:])  # 重要，别忘啦
                return 
            for i in range(startIndex, len(candidates)):
                if sum + candidates[i] >  target: return # 剪枝：如果 sum + candidates[i] > target 就终止遍历
                if i > startIndex and candidates[i]==candidates[i-1]:continue  # 同层重复continue
                sum += candidates[i]
                path.append(candidates[i])
                backtracking(candidates, target, sum, i+1)  
                sum -= candidates[i]
                path.pop()
                
        res, path = [], []
        candidates.sort()
        backtracking(candidates, target, 0, 0)
        return res
    
    class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    public void backtracking(int[] candidates, int target, int count, int[] used, int startIndex){
        if(count == target){
            res.add(new ArrayList<>(path));
            return;
        }
        if(count > target) {
            return;
        }
        for(int i = startIndex; i < candidates.length; i++) {
            if(i > 0 && candidates[i] == candidates[i-1] && used[i-1] == 0){
                continue;
            }
            count += candidates[i];
            path.add(candidates[i]);
            used[i] = 1;
            backtracking(candidates, target, count, used, i+1);
            count -= candidates[i];
            path.remove(path.size()-1);
            used[i] = 0;
        }
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        int[] used = new int[candidates.length];
        Arrays.sort(candidates);
        backtracking(candidates, target, 0, used, 0);
        return res;
    }
}

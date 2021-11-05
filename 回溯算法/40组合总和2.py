class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        used = [0] * len(candidates)
        def backtracking(candidates, target, startIndex, Sum, used):
            if Sum == target:
                res.append(path[:]) # 重要，别忘啦
                return
            if Sum > target: return
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i-1] and used[i-1] == 0: # 同层重复continue
                    continue
                path.append(candidates[i])
                Sum += candidates[i]
                used[i] = 1
                backtracking(candidates, target, i+1, Sum, used)
                path.pop()
                used[i] = 0
                Sum -= candidates[i]
        candidates.sort()  # 树层去重的话，需要对数组排序
        backtracking(candidates, target, 0, 0, used)
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

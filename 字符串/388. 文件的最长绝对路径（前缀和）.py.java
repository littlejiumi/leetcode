class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if '.' not in input: return 0
        res = 0
        depth = {-1: 0}
        temp = []
        for line in input.split('\n'):
            d = line.count('\t')
            depth[d] = depth[d-1] + len(line) - d # 注意'\t'是一个字符
            if line.count('.'):
                res = max(res, depth[d] + d) # 每层都要添加depth个 / 
        return res
/*
用 depth_length_map 保留每层路径的长度，作为前缀和，input.split('\n') 切分为每行分析每行长度与内容
line.count('\t') 的个数来判断是第几层
line.count('.') 的个数判断是否有文件，有文件获取当前最长路径值
每层都要添加 depth 个 / ， 长度需要修改变换
*/
class Solution {
public int lengthLongestPath(String input) {
        int[] lens = new int[input.length() + 1];
        int res = 0;
        for (String line : input.split("\n")) {
            int depth = getDepth(line);
            lens[depth + 1] = lens[depth] + line.length() - depth;   // 防止数组越界，所以 depth + 1 代表本层，depth 代表上一层
            if(line.contains(".")) {  
                res = Math.max(res, lens[depth + 1] + depth);   
            }
        }
        return res;
    }

    private int getDepth(String line) {
        int depth = 0;  
        for (char ch : line.toCharArray()) {
            if (ch == '\t') depth++;
        }
        return depth;
    }
}

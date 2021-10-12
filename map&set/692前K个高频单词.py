# 给一非空的单词列表，返回前 k 个出现次数最多的单词。返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        hash = collections.Counter(words)
        res = sorted(hash, key=lambda word:(-hash[word], word))       
        return res[:k]

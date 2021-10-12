class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        hash = collections.Counter(words)
        res = sorted(hash, key=lambda word:(-hash[word], word))       
        return res[:k]

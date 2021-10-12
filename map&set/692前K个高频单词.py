# 给一非空的单词列表，返回前 k 个出现次数最多的单词。返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        hash = collections.Counter(words)
         # sorted 方法默认正序排列,第一个参数-hash[word] 即单词出现次数的相反数;当词频相同时，用第二个参数 word 进行排序，即字母正序排列
        res = sorted(hash, key=lambda word:(-hash[word], word)) 
        # sorted(hash, key=lambda word:(hash[word], word)) 词频正序， 字母正序
        # sorted(hash, key=lambda word:(hash[word], word), reverse=True) 词频倒序， 字母倒序 （reverse=True 即将sorted方法修改为倒序排列）
        # sorted(hash, key=lambda word:(-hash[word], word), reverse=True) 词频正序， 字母倒序
        return res[:k]

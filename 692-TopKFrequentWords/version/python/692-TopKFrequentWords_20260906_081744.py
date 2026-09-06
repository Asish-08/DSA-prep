# Last updated: 9/6/2026, 8:17:44 AM
1class Solution:
2    def topKFrequent(self, words: List[str], k: int) -> List[str]:
3        count=Counter(words)
4        res=[]
5        for key,val in count.items():
6            res.append([-val,key])
7        res.sort()
8        
9        return [word for freq,word in res[:k]]
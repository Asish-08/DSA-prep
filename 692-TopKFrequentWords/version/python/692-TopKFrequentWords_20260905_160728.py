# Last updated: 9/5/2026, 4:07:28 PM
1class Solution:
2    def topKFrequent(self, words: List[str], k: int) -> List[str]:
3        count=Counter(words)
4        res=[]
5        result=[]
6        for key,val in count.items():
7            res.append([key,val])
8        res.sort(key=lambda x: (-x[1], x[0]))
9        
10        return [word for word,freq in res[:k]]
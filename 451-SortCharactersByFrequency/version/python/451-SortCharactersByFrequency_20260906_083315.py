# Last updated: 9/6/2026, 8:33:15 AM
1class Solution:
2    def frequencySort(self, s: str) -> str:
3        count=Counter(s)
4        maxheap=[]
5        res=""
6
7        for key,val in count.items():
8            heapq.heappush(maxheap,[-val,key])
9        
10        while maxheap:
11            val,key=heapq.heappop(maxheap)
12            while val!=0:
13                res+=key
14                val+=1
15        return res
16
17
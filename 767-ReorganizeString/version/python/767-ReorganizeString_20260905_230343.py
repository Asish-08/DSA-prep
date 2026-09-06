# Last updated: 9/5/2026, 11:03:43 PM
1class Solution:
2    def reorganizeString(self, s: str) -> str:
3        count=Counter(s)
4        heap=[]
5        for key,cnt in count.items():
6            heapq.heappush(heap,(-cnt,key))
7        heapq.heapify(heap)
8
9        prev=None
10        res=""
11        while heap or prev:
12            if prev and not heap:
13                return ""
14            cnt,char=heapq.heappop(heap)
15            res+=char
16            cnt+=1
17
18            if prev:
19                heapq.heappush(heap, prev)
20                prev=None
21            if cnt!=0:
22                prev=(cnt,char)
23        return res
24
25
26            
27
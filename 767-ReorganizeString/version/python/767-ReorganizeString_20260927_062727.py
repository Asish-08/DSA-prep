# Last updated: 9/27/2026, 6:27:27 AM
1class Solution:
2    def reorganizeString(self, s: str) -> str:
3        count=Counter(s)
4        res=""
5        heap=[]
6        for key,val in count.items():
7            heap.append((-val,key))
8        heapq.heapify(heap)
9        prev=None
10
11        while heap or prev:
12            if heap==[] and prev:
13                return ""
14            cnt,char=heapq.heappop(heap)
15            res+=char
16            cnt+=1
17            if prev:
18                heapq.heappush(heap,prev)
19                prev=None
20            if cnt!=0:
21                prev=(cnt,char)
22        return res
23            
24
25
26
27
28
29        
30
31        # count=Counter(s)
32        # heap=[]
33        # for key,cnt in count.items():
34        #     heap.append((-cnt,key))
35        # heapq.heapify(heap)
36
37        # prev=None
38        # res=""
39        # while heap or prev:
40        #     if prev and not heap:
41        #         return ""
42        #     cnt,char=heapq.heappop(heap)
43        #     res+=char
44        #     cnt+=1
45
46        #     if prev:
47        #         heapq.heappush(heap, prev)
48        #         prev=None
49        #     if cnt!=0:
50        #         prev=(cnt,char)
51        # return res
52
53
54            
55
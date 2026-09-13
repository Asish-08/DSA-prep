# Last updated: 9/12/2026, 5:48:03 PM
1class Solution:
2    def reorganizeString(self, s: str) -> str:
3        count=Counter(s)
4        heap=[]
5        for key,val in count.items():
6            heap.append((-val,key))
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
19                heapq.heappush(heap,prev)
20                prev=None
21            if cnt!=0:
22                prev=(cnt,char)
23        return res
24
25        # count=Counter(s)
26        # heap=[]
27        # for key,cnt in count.items():
28        #     heap.append((-cnt,key))
29        # heapq.heapify(heap)
30
31        # prev=None
32        # res=""
33        # while heap or prev:
34        #     if prev and not heap:
35        #         return ""
36        #     cnt,char=heapq.heappop(heap)
37        #     res+=char
38        #     cnt+=1
39
40        #     if prev:
41        #         heapq.heappush(heap, prev)
42        #         prev=None
43        #     if cnt!=0:
44        #         prev=(cnt,char)
45        # return res
46
47
48            
49
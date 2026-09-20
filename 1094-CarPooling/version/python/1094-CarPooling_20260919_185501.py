# Last updated: 9/19/2026, 6:55:01 PM
1class Solution:
2    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
3        trips.sort(key=lambda t:t[1])
4        minheap=[]
5        curPass=0
6        for t in trips:
7            numPass,start,end=t
8            while minheap and start>=minheap[0][0]:
9                curPass-=minheap[0][1]
10                heapq.heappop(minheap)
11            curPass+=numPass
12            if curPass>capacity:
13                return False
14
15            heapq.heappush(minheap, [end,numPass])
16        return True
17
18
19
20
21
22
23
24
25        # trips.sort(key=lambda t:t[1])
26        # minheap=[]
27        # curPass=0
28
29        # for t in trips:
30        #     numPass,start,end=t
31        #     while minheap and start>=minheap[0][0]:
32        #         curPass-=minheap[0][1]
33        #         heapq.heappop(minheap)
34        #     curPass+=numPass
35
36        #     if curPass > capacity:
37        #         return False
38        #     heapq.heappush(minheap, [end,numPass])
39        # return True
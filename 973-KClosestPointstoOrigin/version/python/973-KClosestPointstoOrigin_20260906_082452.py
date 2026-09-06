# Last updated: 9/6/2026, 8:24:52 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        # res=[]
4        # min_heap=[]
5
6        # for x,y in points:
7        #     dist=x**2+y**2
8        #     min_heap.append([dist,x,y])
9        # heapq.heapify(min_heap)
10        # while k:
11        #     dist,x,y=heapq.heappop(min_heap)
12        #     res.append([x,y])
13        #     k-=1
14        # return res
15        res=[]
16        minheap=[]
17        for x,y in points:
18            dist=x**2 + y**2
19            heapq.heappush(minheap,[dist,x,y])
20        
21        while k:
22            dist,x,y=heapq.heappop(minheap)
23            res.append([x,y])
24            k-=1
25        return res
26
27            
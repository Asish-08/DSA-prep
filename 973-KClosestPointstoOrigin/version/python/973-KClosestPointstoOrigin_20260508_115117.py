# Last updated: 5/8/2026, 11:51:17 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        res=[]
4        min_heap=[]
5
6        for x,y in points:
7            dist=x**2+y**2
8            min_heap.append([dist,x,y])
9        heapq.heapify(min_heap)
10        while k:
11            dist,x,y=heapq.heappop(min_heap)
12            res.append([x,y])
13            k-=1
14        return res
15            
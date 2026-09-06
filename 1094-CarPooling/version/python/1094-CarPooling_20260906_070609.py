# Last updated: 9/6/2026, 7:06:09 AM
1class Solution:
2    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
3        trips.sort(key=lambda t:t[1])
4        minheap=[]
5        curPass=0
6
7        for t in trips:
8            numPass,start,end=t
9            while minheap and start>=minheap[0][0]:
10                curPass-=minheap[0][1]
11                heapq.heappop(minheap)
12            curPass+=numPass
13
14            if curPass > capacity:
15                return False
16            heapq.heappush(minheap, [end,numPass])
17        return True
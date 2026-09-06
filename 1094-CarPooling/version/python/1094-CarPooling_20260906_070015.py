# Last updated: 9/6/2026, 7:00:15 AM
1class Solution:
2    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
3        trips.sort(key=lambda t:t[1])
4        minheap=[] # [end, numPass] pairs created
5        curPass=0
6        for t in trips:
7            numPass,start,end=t
8            while minheap and start>=minheap[0][0]:
9                curPass-=minheap[0][1]
10                heapq.heappop(minheap)
11            curPass+=numPass
12            if curPass > capacity:
13                return False
14            heapq.heappush(minheap,[end,numPass])
15        return True
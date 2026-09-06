# Last updated: 9/5/2026, 10:09:30 PM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        if not intervals:
4            return 0
5        heap=[]
6        intervals.sort(key=lambda x:x[0])
7        for start,end in intervals:
8            if heap and start>=heap[0]:
9                heapq.heappop(heap)
10            heapq.heappush(heap,end)
11        return len(heap)
12
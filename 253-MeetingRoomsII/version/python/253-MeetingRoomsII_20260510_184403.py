# Last updated: 5/10/2026, 6:44:03 PM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        if not intervals:
4            return 0
5        heap=[]
6        intervals.sort(key=lambda x:x[0])
7        for meeting in intervals:
8            start,end=meeting
9            if heap and heap[0]<=start:
10                heapq.heappop(heap)
11            heapq.heappush(heap,end)
12        return len(heap)
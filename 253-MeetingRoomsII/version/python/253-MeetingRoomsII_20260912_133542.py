# Last updated: 9/12/2026, 1:35:42 PM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        heap=[]
4        intervals.sort(key=lambda x:x[0])
5        for start,end in intervals:
6            if heap and start>=heap[0]:
7                heapq.heappop(heap)
8            heapq.heappush(heap,end)
9        return len(heap)
10        
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29        # if not intervals:
30        #     return 0
31        # heap=[]
32        # intervals.sort(key=lambda x:x[0])
33        # for start,end in intervals:
34        #     if heap and start>=heap[0]:
35        #         heapq.heappop(heap)
36        #     heapq.heappush(heap,end)
37        # return len(heap)
38
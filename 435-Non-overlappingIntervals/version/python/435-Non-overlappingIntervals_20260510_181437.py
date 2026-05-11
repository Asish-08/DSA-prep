# Last updated: 5/10/2026, 6:14:37 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x:x[1])
4        #[[1,2],[1,3],[2,3],[3,4]]
5        prevEnd=float('-inf')
6        removeCount=0
7        for start,end in intervals:
8            if start>=prevEnd:
9                prevEnd=end
10            else:
11                removeCount+=1
12        return removeCount
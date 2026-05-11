# Last updated: 5/10/2026, 6:07:36 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        merged=[intervals[0]]
5        for interval in intervals[1:]:
6            if interval[0]<=merged[-1][1]:
7                merged[-1][1]=max(merged[-1][1],interval[1])
8            else:
9                merged.append(interval)
10        return merged
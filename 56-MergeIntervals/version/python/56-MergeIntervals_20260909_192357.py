# Last updated: 9/9/2026, 7:23:57 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        merged=[intervals[0]]
5        for interval in intervals:
6            if merged[-1][1]>=interval[0]: #check the sign
7                merged[-1][1]=max(merged[-1][1],interval[1])
8            else:
9                merged.append(interval)
10        return merged
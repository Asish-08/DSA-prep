# Last updated: 5/10/2026, 5:52:32 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res = []
4
5        for i in range(len(intervals)):
6
7            # Case 1: newInterval comes before the current interval
8            # Example: newInterval = [-1, 0], current = [1, 3]
9            if newInterval[1] < intervals[i][0]:
10                res.append(newInterval)
11                return res + intervals[i:]
12
13            # Case 2: current interval comes before newInterval
14            # Example: current = [1, 2], newInterval = [4, 5]
15            elif newInterval[0] > intervals[i][1]:
16                res.append(intervals[i])
17
18            # Case 3: newInterval overlaps with the current interval
19            # Example: newInterval = [1, 3], current = [2, 6]
20            else:
21                newInterval = [
22                    min(newInterval[0], intervals[i][0]),
23                    max(newInterval[1], intervals[i][1])
24                ]
25
26        res.append(newInterval)
27        return res
# Last updated: 5/10/2026, 6:19:36 PM
1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        intervals.sort()
4        for i in range(len(intervals)-1):
5            if intervals[i][1]>intervals[i+1][0]:
6                return False
7            else:
8                continue
9        return True
# Last updated: 5/10/2026, 12:10:28 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        before_house=0
4        before_two_houses=0
5
6        for n in nums:
7            temp=max(n+before_house,before_two_houses)
8            before_house=before_two_houses
9            before_two_houses=temp
10        return before_two_houses
11            
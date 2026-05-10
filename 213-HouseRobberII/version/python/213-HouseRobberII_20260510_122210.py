# Last updated: 5/10/2026, 12:22:10 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        def rob_linear(houses):
4            two_houses_before=0
5            before_house=0
6
7            for n in houses:
8                curr=max(n+two_houses_before,before_house)
9                two_houses_before=before_house
10                before_house=curr
11            return before_house
12
13        if len(nums)==1:
14            return nums[0]
15        return max (rob_linear(nums[1:]), rob_linear(nums[:-1]))
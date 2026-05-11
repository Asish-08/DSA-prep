# Last updated: 5/10/2026, 7:22:57 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        goal=len(nums)-1
4        for i in range(len(nums)-1,-1,-1):
5            if i+nums[i]>=goal:
6                goal=i
7        return True if not goal else False
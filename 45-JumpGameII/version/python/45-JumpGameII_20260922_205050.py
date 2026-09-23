# Last updated: 9/22/2026, 8:50:50 PM
1class Solution:
2    def jump(self, nums: list[int]) -> int:
3        steps=0
4        l,r=0,0
5
6        while r<len(nums)-1:
7            farthest=0
8            for i in range(l,r+1):
9                farthest=max(farthest,i+nums[i])
10            l=r+1
11            r=farthest
12            steps+=1
13        return steps
14
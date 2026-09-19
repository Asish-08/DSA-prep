# Last updated: 9/18/2026, 9:58:02 PM
1class Solution:
2    def nextGreaterElements(self, nums: list[int]) -> list[int]:
3        N=len(nums)
4        res=[-1]*N
5        stack=[]
6
7        for i in range(2*N):
8            while stack and nums[stack[-1]]< nums[i%N]:
9                idx=stack.pop()
10                res[idx]=nums[i%N]
11            if i<N:
12                stack.append(i)
13        return res
14
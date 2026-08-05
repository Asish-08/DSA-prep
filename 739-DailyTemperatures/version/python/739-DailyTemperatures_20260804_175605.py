# Last updated: 8/4/2026, 5:56:05 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res=[0]*len(temperatures)
4        stack=[]
5        for i,temp in enumerate(temperatures):
6            #
7            while stack and stack[-1][1]<temp:
8                stack_idx,stack_temp=stack.pop()
9                res[stack_idx]=i-stack_idx
10            stack.append([i,temp])
11        return res
12                
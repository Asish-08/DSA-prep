# Last updated: 3/30/2026, 5:19:47 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res=[0]*len(temperatures)
4        stack=[]
5        for i,temp in enumerate(temperatures):
6            while stack and temp>stack[-1][1]:
7                stack_index,stack_temp=stack.pop()
8                res[stack_index]=i-stack_index
9            stack.append([i,temp])
10        return res
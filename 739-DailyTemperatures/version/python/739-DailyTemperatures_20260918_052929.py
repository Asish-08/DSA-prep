# Last updated: 9/18/2026, 5:29:29 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        # res=[0]*len(temperatures)
4        # stack=[]
5        # for i,temp in enumerate(temperatures):
6        #     while stack and temperatures[stack[-1]]<temp:
7        #         stack_idx=stack.pop()
8        #         res[stack_idx]=i-stack_idx
9        #     stack.append(i)
10        # return res
11        res=[0]*len(temperatures)
12        stack=[]
13        for i,temp in enumerate(temperatures):
14            while stack and temperatures[stack[-1]]< temp:
15                stack_idx=stack.pop()
16                res[stack_idx]+=i-stack_idx
17            stack.append(i)
18        return res
19
20                
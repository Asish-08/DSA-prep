# Last updated: 8/11/2026, 4:21:28 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        maxarea=0
4        stack=[]
5
6        for i,h in enumerate(heights):
7            start=i
8            while stack and stack[-1][1]>h:
9                index,height=stack.pop()
10                area=(i-index)*height
11                maxarea=max(maxarea,area)
12                start=index
13            stack.append([start,h])
14        for i,h in stack:
15            maxarea=max(maxarea,h*(len(heights)-i))
16        return maxarea
17    
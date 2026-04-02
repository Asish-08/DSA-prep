# Last updated: 4/2/2026, 4:46:22 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        maxArea=0
4        stack=[]
5        for i,h in enumerate(heights):
6            start=i
7            while stack and stack[-1][1]>h:
8                index,height=stack.pop()
9                maxArea=max(maxArea, height*(i-index))
10                start=index
11            stack.append((start,h))
12        for i,h in stack:
13            maxArea=max(maxArea,h* (len(heights)-i))
14        return maxArea
15        
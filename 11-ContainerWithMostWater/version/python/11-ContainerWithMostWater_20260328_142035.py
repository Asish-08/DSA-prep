# Last updated: 3/28/2026, 2:20:35 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l,r=0,len(height)-1
4        max_area=0
5        while l<r:
6            h=min(height[l],height[r])
7            curr_area=(r-l)*h
8            if height[l]<height[r]:
9                l+=1
10            elif height[l]>=height[r]:
11                r-=1
12            max_area=max(curr_area,max_area)
13        return max_area
14            
15
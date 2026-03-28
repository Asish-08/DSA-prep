# Last updated: 3/28/2026, 2:31:48 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l,r=0,len(height)-1
4        res=0
5        left_max,right_max=0,0
6        while l<r:
7            if height[l]<height[r]:
8                left_max=max(left_max,height[l])
9                res+=left_max-height[l]
10                l+=1
11            else:
12                right_max=max(right_max,height[r])
13                res+=right_max-height[r]
14                r-=1
15        return res
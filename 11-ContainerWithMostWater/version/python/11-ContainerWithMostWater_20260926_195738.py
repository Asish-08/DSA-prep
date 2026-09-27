# Last updated: 9/26/2026, 7:57:38 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        # l,r=0,len(height)-1
4        # max_area=0
5        # while l<r:
6        #     h=min(height[l],height[r])
7        #     curr_area=(r-l)*h
8        #     if height[l]<height[r]:
9        #         l+=1
10        #     else:
11        #         r-=1
12        #     max_area=max(curr_area,max_area)
13        # return max_area
14        l,r=0,len(height)-1
15        max_area=0
16        while l<r:
17            h=min(height[l],height[r])
18            cur_area=h*(r-l)
19            max_area=max(max_area,cur_area)
20            if h==height[l]:
21                l+=1
22            else:
23                r-=1
24        return max_area
25            # if height[l]<height[r]:
26            #     curr_area=height[l]* (r-l)
27            #     max_area=max(max_area,curr_area)
28            #     l+=1
29            # else:
30            #     curr_area=height[r]* (r-l)
31            #     max_area=max(max_area,curr_area)
32            #     r-=1
33        return max_area
34
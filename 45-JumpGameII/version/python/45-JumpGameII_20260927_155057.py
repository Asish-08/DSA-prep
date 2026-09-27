# Last updated: 9/27/2026, 3:50:57 PM
1class Solution:
2    def jump(self, nums: list[int]) -> int:
3        steps=0
4        l,r=0,0
5        while r<len(nums)-1:
6            farthest=0
7            for i in range(l,r+1):
8                farthest=max(farthest,i+nums[i])
9            l=r+1
10            r=farthest
11            steps+=1
12        return steps
13
14
15
16        # steps=0
17        # l,r=0,0
18        # while r<len(nums)-1:
19        #     farthest=0
20        #     for i in range(l,r+1):
21        #         farthest=max(farthest,i+nums[i])
22        #     l=r+1
23        #     r=farthest
24        #     steps+=1
25        # return steps
# Last updated: 9/10/2026, 6:44:44 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        res=[]
5        for i in range(len(nums)-2):
6
7
8                l=i+1
9                r=len(nums)-1
10                if i>0 and nums[i]==nums[i-1]:
11                    continue
12                while l<r:
13                    total=nums[i]+nums[l]+nums[r]
14                    if total==0:
15                        res.append([nums[i],nums[l],nums[r]])
16                        l+=1
17                        r-=1
18                        while l<r and nums[l]==nums[l-1]:
19                            l+=1
20                        while l<r and nums[r]==nums[r+1]:
21                            r-=1
22                    elif total<0:
23                        l+=1
24                    else:
25                        r-=1
26        return res
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46        # nums.sort()
47        # res=[]
48        # for i in range(len(nums)-2):
49        #     l=i+1
50        #     r=len(nums)-1
51        #     if i >0 and nums[i]==nums[i-1]:
52        #             continue
53        #     while l<r:
54        #         total=nums[i]+nums[l]+nums[r]
55        #         if total==0:
56        #             res.append([nums[i],nums[l],nums[r]])
57        #             l+=1
58        #             r-=1
59        #             while l<r and nums[l]==nums[l-1]:
60        #                 l+=1
61        #             while l<r and nums[r]==nums[r+1]:
62        #                 r-=1
63        #         elif total < 0:
64        #             l+=1
65        #         else:
66        #             r-=1
67                
68        # return res
69
70
71
# Last updated: 9/20/2026, 5:19:45 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        prefix,suffix=1,1
5        res=[1]*n
6
7        for i in range(n):
8            res[i]=prefix
9            prefix*=nums[i]
10        for i in range(n-1,-1,-1):
11            res[i]*=suffix
12            suffix*=nums[i]
13        return res
14
15
16
17
18
19
20
21        # n=len(nums)
22        # res=[1]*n
23        # prefix=1
24        # suffix=1
25
26        # for i in range(n):
27        #     res[i]=prefix
28        #     prefix*=nums[i]
29        #     print(res)
30        
31        # for i in range(n-1,-1,-1):
32        #     res[i]*=suffix
33        #     suffix*=nums[i]
34        #     print(res)
35        
36        # return res
37        
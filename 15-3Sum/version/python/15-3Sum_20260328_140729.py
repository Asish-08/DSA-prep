# Last updated: 3/28/2026, 2:07:29 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        res=[]
5        for i in range(len(nums)-2):
6            l=i+1
7            r=len(nums)-1
8            if i >0 and nums[i]==nums[i-1]:
9                    continue
10            while l<r:
11                total=nums[i]+nums[l]+nums[r]
12                if total==0:
13                    res.append([nums[i],nums[l],nums[r]])
14                    l+=1
15                    r-=1
16                    while l<r and nums[l]==nums[i-1]:
17                        l+=1
18                    while l<r and nums[r]==nums[r+1]:
19                        r-=1
20                elif total < 0:
21                    l+=1
22                else:
23                    r-=1
24                
25        return res
26
27
28
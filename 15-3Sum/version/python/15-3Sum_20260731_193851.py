# Last updated: 7/31/2026, 7:38:51 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        if not nums:
4            return []
5        res,quad=[],[]
6        nums.sort()
7        def ksum(k, start, target):
8            if k!=2:
9                for i in range(start, len(nums)-k+1):
10                    if i>start and nums[i]==nums[i-1]:
11                        continue
12                    quad.append(nums[i])
13                    ksum(k-1, i+1, target-nums[i])
14                    quad.pop()
15                return
16            l,r=start,len(nums)-1
17            while l<r:
18                total=nums[l]+nums[r]
19                if total>target:
20                    r-=1
21                elif total<target:
22                    l+=1
23                else:
24                    res.append(quad+[nums[l],nums[r]])
25                    l+=1
26                    while l<r and nums[l]==nums[l-1]:
27                        l+=1
28        ksum(4,0,target)
29        return res
30
31
32
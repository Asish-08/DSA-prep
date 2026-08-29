# Last updated: 8/28/2026, 5:55:45 PM
1class Solution:
2    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
3        res=0
4        odd=0
5        l,m=0,0
6
7        for r in range(len(nums)):
8            if nums[r]%2:
9                odd+=1
10            while odd>k:
11                if nums[l]%2:
12                    odd-=1
13                l+=1
14                m=l
15
16            if odd==k:
17                while not nums[m]%2:
18                    m+=1
19                res+=(m-l+1)
20        return res
# Last updated: 8/27/2026, 4:38:09 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        l,r=0,len(nums)-1
4        while l< r:
5            mid=l+(r-l)//2
6            half_even=(r-mid)%2==0
7            if nums[mid+1]==nums[mid]:
8                if half_even:
9                    l=mid+2
10                else:
11                    r=mid-1
12            elif nums[mid-1]==nums[mid]:
13                if  half_even:
14                    r=mid-2
15                else:
16                    l=mid+1
17            else:
18                return nums[mid]
19        return nums[l]
20
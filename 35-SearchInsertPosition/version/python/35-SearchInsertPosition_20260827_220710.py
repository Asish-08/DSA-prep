# Last updated: 8/27/2026, 10:07:10 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        l,r=0,len(nums)-1
4        while l<=r:
5            mid=(l+r)//2
6            if nums[mid]<target:
7                l=mid+1
8            elif nums[mid]>target:
9                r=mid-1
10            else:
11                return mid
12        return l
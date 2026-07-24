# Last updated: 7/23/2026, 5:00:19 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l,r=0,len(nums)-1
4        while l<=r:
5            mid=(l+r)//2
6            if nums[mid]==target:
7                return mid
8            elif nums[mid]>target:
9                r=mid-1
10            else:
11                l=mid+1
12        return -1
13            
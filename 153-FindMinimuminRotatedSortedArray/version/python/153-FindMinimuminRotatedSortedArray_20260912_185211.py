# Last updated: 9/12/2026, 6:52:11 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        # l,r=0,len(nums)-1
4        # while l<r:
5        #     mid=(l+r)//2
6        #     if nums[mid]>nums[r]:
7        #         l=mid+1
8        #     elif nums[mid]<nums[r]:
9        #         r=mid
10        # return nums[l]
11        l,r=0,len(nums)-1
12        while l<r:
13            mid=(l+r)//2
14            if nums[mid]>nums[r]:
15                l=mid+1
16            elif nums[mid]<nums[r]:
17                r=mid
18        return nums[l]
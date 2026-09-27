# Last updated: 9/27/2026, 7:23:17 AM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        l,r=0,len(nums)-1
4        while l<=r:
5            mid=(l+r)//2
6            if nums[mid]==target:
7                return mid
8            elif nums[mid]<target:
9                l=mid+1
10            else:
11                r=mid-1
12        return l
13
14
15
16
17        # l,r=0,len(nums)-1
18        # while l<=r:
19        #     mid=(l+r)//2
20        #     if nums[mid]<target:
21        #         l=mid+1
22        #     elif nums[mid]>target:
23        #         r=mid-1
24        #     else:
25        #         return mid
26        # return l
# Last updated: 8/27/2026, 5:06:19 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        l,r=0,len(nums)-1
4        while l<r:
5            mid=(l+r)//2
6            if mid%2==1:
7                mid-=1
8            if nums[mid]==nums[mid+1]:
9                l=mid+2
10            else:
11                r=mid
12        return nums[l]
13                
14            
15        # l,r=0,len(nums)-1
16        # while l< r:
17        #     mid=l+(r-l)//2
18        #     half_even=(r-mid)%2==0
19        #     if nums[mid+1]==nums[mid]:
20        #         if half_even:
21        #             l=mid+2
22        #         else:
23        #             r=mid-1
24        #     elif nums[mid-1]==nums[mid]:
25        #         if  half_even:
26        #             r=mid-2
27        #         else:
28        #             l=mid+1
29        #     else:
30        #         return nums[mid]
31        # return nums[l]
32
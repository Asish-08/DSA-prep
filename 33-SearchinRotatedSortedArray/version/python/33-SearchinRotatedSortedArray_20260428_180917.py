# Last updated: 4/28/2026, 6:09:17 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l,r=0,len(nums)-1
4        while l<=r:
5            mid=(l+r)//2
6            if nums[mid]==target:
7                return mid
8            if nums[l]<=nums[mid]:
9                if nums[l]<=target<nums[mid]:
10                    r=mid-1
11                else:
12                    l=mid+1
13            else:
14                if nums[mid]<target<=nums[r]:
15                    l=mid+1
16                else:
17                    r=mid-1
18                
19        return -1
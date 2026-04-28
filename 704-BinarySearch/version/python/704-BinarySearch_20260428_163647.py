# Last updated: 4/28/2026, 4:36:47 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l,r=0,len(nums)-1
4        while l<=r:
5            mid=(l+r)//2
6            if nums[mid]==target:
7                return mid
8                break
9            elif nums[mid]>target:
10                r=mid-1
11            else:
12                l=mid+1
13        return -1
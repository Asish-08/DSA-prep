# Last updated: 8/27/2026, 8:26:40 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[r]:
                r=mid-1
            else:
                return nums[mid]
        return nums[l]
# Last updated: 8/12/2026, 5:11:04 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return r+1
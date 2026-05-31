# Last updated: 5/30/2026, 6:46:00 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        if not nums:
            return 0
        while val in nums:
            nums.remove(val)
        return len(nums)

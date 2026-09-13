# Last updated: 9/12/2026, 8:13:16 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # new = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[new] = nums[i]
        #         new += 1
        # return new
        new = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[new] = nums[i]
                new += 1

        return new
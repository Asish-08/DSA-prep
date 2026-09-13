# Last updated: 9/12/2026, 8:10:39 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        if not nums:
4            return 0
5        while val in nums:
6            nums.remove(val)
7        return len(nums)
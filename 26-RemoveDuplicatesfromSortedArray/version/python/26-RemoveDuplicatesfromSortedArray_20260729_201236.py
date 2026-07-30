# Last updated: 7/29/2026, 8:12:36 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        k=1
6        for i in range(1,len(nums)):
7            if nums[i]!=nums[i-1]:
8                nums[k]=nums[i]
9                k+=1
10        return k
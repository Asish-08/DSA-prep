# Last updated: 9/23/2026, 7:51:17 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        k=0
7        for i in range(len(nums)):
8            if nums[i]!=0:
9                nums[k]=nums[i]
10                k+=1
11        # print(nums)
12
13        for i in range(k,len(nums)):
14            nums[i]=0
15        
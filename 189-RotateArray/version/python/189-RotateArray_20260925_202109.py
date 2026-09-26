# Last updated: 9/25/2026, 8:21:09 PM
1class Solution:
2    def rotate(self, nums: list[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n=len(nums)
7        k=k%n
8        def rev(l,r):
9            while l<r:
10                nums[l],nums[r]=nums[r],nums[l]
11                l+=1
12                r-=1
13        
14        rev(0,n-1)
15        rev(0,k-1)
16        rev(k,n-1)
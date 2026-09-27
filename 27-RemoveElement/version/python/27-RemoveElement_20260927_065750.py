# Last updated: 9/27/2026, 6:57:50 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k=0
4        for i in range(len(nums)):
5            if nums[i]!=val:
6                nums[k]=nums[i]
7                k+=1
8        return k
9
10
11
12        # if not nums:
13        #     return 0
14        # l=0
15        # for i in range(len(nums)):
16        #     if nums[i]!=val:
17        #         nums[l]=nums[i]
18        #         l+=1
19        # return l
20            
21        # if not nums:
22        #     return 0
23        # while val in nums:
24        #     nums.remove(val)
25        # return len(nums)
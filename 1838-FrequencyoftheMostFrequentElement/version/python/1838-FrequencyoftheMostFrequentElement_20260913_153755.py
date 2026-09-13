# Last updated: 9/13/2026, 3:37:55 PM
1class Solution:
2    def maxFrequency(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        left,result,total=0,0,0
5
6        for right in range(len(nums)):
7            total+=nums[right]
8            while nums[right]*(right-left+1)-total>k:
9                total-=nums[left]
10                left+=1
11            result=max(result,right-left+1)
12        return result
13
14                
15
16        # nums.sort()
17        # left,total,result=0,0,0
18
19        # for right in range(len(nums)):
20        #     total+=nums[right]
21
22        #     # If the cost to make every number in the window equal to nums[right] exceeds k, shrink the window from the left.
23        #     while nums[right]*(right-left+1)-total>k:
24        #         total-=nums[left]
25        #         left+=1
26        #     result=max(result,right-left+1)
27        # return result
28
29
30
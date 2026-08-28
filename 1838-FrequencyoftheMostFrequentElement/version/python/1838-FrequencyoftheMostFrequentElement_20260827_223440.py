# Last updated: 8/27/2026, 10:34:40 PM
1class Solution:
2    def maxFrequency(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        left,total,result=0,0,0
5
6        for right in range(len(nums)):
7            total+=nums[right]
8
9            # If the cost to make every number in the window equal to nums[right] exceeds k, shrink the window from the left.
10            while nums[right]*(right-left+1)-total>k:
11                total-=nums[left]
12                left+=1
13            result=max(result,right-left+1)
14        return result
15
16
17
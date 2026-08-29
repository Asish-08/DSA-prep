# Last updated: 8/29/2026, 1:35:11 PM
1class Solution:
2    def minSwaps(self, nums: List[int]) -> int:
3        N=len(nums)
4        window_ones,max_window_ones=0,0
5        left=0
6        total=nums.count(1)
7
8        for right in range(2*N):
9            if nums[right%N]:
10                window_ones+=1
11            if right-left+1>total:
12                window_ones-=nums[left%N]
13                left+=1
14            max_window_ones=max(max_window_ones,window_ones)
15        return total-max_window_ones
16
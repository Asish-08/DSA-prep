# Last updated: 8/29/2026, 12:23:57 PM
1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        ans=0
4        start=-1
5        freq=Counter()
6        for end in range(len(nums)):
7            freq[nums[end]]+=1
8
9            while freq[nums[end]]>k:
10                start+=1
11                freq[nums[start]]-=1
12            ans=max(ans,end-start)
13        return ans
14
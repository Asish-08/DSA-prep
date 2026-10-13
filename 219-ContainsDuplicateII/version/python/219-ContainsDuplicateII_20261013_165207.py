# Last updated: 10/13/2026, 4:52:07 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        # seen = {}
4        # for i, num in enumerate(nums):
5        #     if num in seen and i - seen[num] <= k:
6        #         # If the number has been seen before and the difference between
7        #     # the current index and the last seen index is less than or equal to k
8        #         return True
9        #     seen[num] = i
10        # return False
11
12        seen={}
13        for i, n in enumerate(nums):
14            if n  in seen and i-seen[n]<=k:
15                return True
16            seen[n]=i
17        return False
# Last updated: 3/24/2026, 11:12:13 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen=set()
4        for i in nums:
5            seen.add(i)
6        return len(seen)!=len(nums)
# Last updated: 5/5/2026, 8:21:11 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        nums_seen=set()
4        for num in nums:
5            if num in nums_seen:
6                return num
7            nums_seen.add(num)
8        return False
9
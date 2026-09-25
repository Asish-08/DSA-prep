# Last updated: 9/24/2026, 11:17:28 PM
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        min_num=min(nums1)
4
5        if min_num%2==1:
6            return True
7        
8        for num in nums1:
9            if num%2==1:
10                return False
11        return True
# Last updated: 9/24/2026, 11:19:58 PM
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        #odd-even=odd; even-odd=odd
4
5        min_num=min(nums1)
6        if min_num%2==1:
7            return True
8        
9        for num in nums1:
10            if num%2==1:
11                return False
12        return True
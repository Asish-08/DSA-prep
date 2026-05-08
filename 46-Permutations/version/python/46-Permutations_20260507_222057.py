# Last updated: 5/7/2026, 10:20:57 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res=[]
4        def backtrack(curr):
5            if len(curr)==len(nums):
6                res.append(curr[:])
7                return
8            for num in nums:
9                if num not in curr:
10                    curr.append(num)
11                    backtrack(curr)
12                    curr.pop()
13        backtrack([])
14        return res
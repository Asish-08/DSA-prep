# Last updated: 9/5/2026, 5:43:02 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        path=[]
4        res=[]
5
6        def backtrack(curr):
7            if len(path)==len(curr):
8                res.append(path[:])
9                return
10            for num in curr:
11                if num not in path:
12                    path.append(num)
13                    backtrack(curr)
14                    path.pop()
15
16        backtrack(nums)
17        return res
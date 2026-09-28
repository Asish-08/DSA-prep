# Last updated: 9/27/2026, 5:49:34 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        # res=[]
4        # subset=[]
5
6        # def dfs(i):
7        #     if i>=len(nums):
8        #         res.append(subset.copy())
9        #         return
10            
11        #     #decision to include nums[i]
12        #     subset.append(nums[i])
13        #     dfs(i+1)
14
15        #     #decision to NOT include nums[i]
16        #     subset.pop()
17        #     dfs(i+1)
18
19        # dfs(0)
20        # return res
21
22        res=[]
23        subset=[]
24        def dfs(i):
25            if i>=len(nums):
26                res.append(subset.copy())
27                return
28            
29            subset.append(nums[i])
30            dfs(i+1)
31
32            subset.pop()
33            dfs(i+1)
34        dfs(0)
35        return res
36            
# Last updated: 9/12/2026, 6:36:09 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        # n=len(nums)
4        # res=[0]*(n*2)
5        
6        # for i in range(len(res)):
7        #     if i<n:
8        #         res[i]=nums[i]
9        #     else:
10        #         res[i]=nums[i-n]
11        # return res
12        n=len(nums)
13        res=[0]*(n*2)
14
15        for i in range(len(res)):
16            if i<n:
17                res[i]=nums[i]
18            else:
19                res[i]=nums[i-n]
20        return res
21
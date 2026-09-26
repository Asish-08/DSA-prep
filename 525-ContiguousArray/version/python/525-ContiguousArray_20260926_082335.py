# Last updated: 9/26/2026, 8:23:35 AM
1class Solution:
2    def findMaxLength(self, nums: List[int]) -> int:
3        zeros,ones=0,0
4        diff_index={}
5        res=0
6
7        for i,num in enumerate(nums):
8            if num==0:
9                zeros+=1
10            else:
11                ones+=1
12            if ones-zeros not in diff_index:
13                diff_index[ones-zeros]=i
14            if ones==zeros:
15                res=ones+zeros
16            else:
17                idx=diff_index[ones-zeros]
18                res=max(res,i-idx)
19        return res
# Last updated: 3/27/2026, 7:08:11 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        long_streak=0
4        num_set=set(nums)
5        for n in num_set:
6            if n-1 not in num_set:
7                curr_num=n
8                curr_streak=1
9                while curr_num+1 in num_set:
10                    curr_num+=1
11                    curr_streak+=1
12                long_streak=max(long_streak, curr_streak)
13        return long_streak
# Last updated: 9/21/2026, 4:57:37 PM
1from collections import Counter
2class Solution:
3    def deleteAndEarn(self, nums: list[int]) -> int:
4        h_map=Counter(nums)
5        uniq=sorted(h_map.keys())
6        take,skip=0,0
7        prev=-1
8
9        for num in uniq:
10            points=num*h_map[num]           # Total points from taking all occurrences
11            if num==prev+1:                 # Current and previous numbers conflict
12                new_take=skip+points        # Take current, so previous must be skipped
13                new_skip=max(skip,take)     # Skip current, keep previous best
14            else:
15                best=max(skip,take)
16                new_take=best+points
17                new_skip=best
18            take=new_take
19            skip=new_skip
20            prev=num
21        return max(take,skip)
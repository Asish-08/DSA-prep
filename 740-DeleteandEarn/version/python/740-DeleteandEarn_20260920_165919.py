# Last updated: 9/20/2026, 4:59:19 PM
1from collections import Counter
2class Solution:
3    def deleteAndEarn(self, nums: list[int]) -> int:
4        count = Counter(nums)
5        unique = sorted(count.keys())
6
7        take=0
8        skip=0
9        prev=-1
10
11        for num in unique:
12            points=num*count[num]
13
14            if num==prev+1:
15                new_take=skip+points
16                new_skip=max(take,skip)
17            else:
18                best=max(take,skip)
19                new_take=best+points
20                new_skip=best
21            take=new_take
22            skip=new_skip
23            prev=num
24        return max(take,skip)
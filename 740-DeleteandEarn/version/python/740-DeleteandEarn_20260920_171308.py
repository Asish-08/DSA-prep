# Last updated: 9/20/2026, 5:13:08 PM
1from collections import Counter
2class Solution:
3    def deleteAndEarn(self, nums: list[int]) -> int:
4        h_map=Counter(nums)
5        uniq=sorted(h_map.keys())
6        take,skip=0,0
7        prev=-1
8
9        for num in uniq:
10            points=num*h_map[num]
11            if num==prev+1:
12                new_take=skip+points
13                new_skip=max(skip,take)
14            else:
15                best=max(skip,take)
16                new_take=best+points
17                new_skip=best
18            take=new_take
19            skip=new_skip
20            prev=num
21        return max(take,skip)
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36        # count = Counter(nums)
37        # unique = sorted(count.keys())
38
39        # take=0
40        # skip=0
41        # prev=-1
42
43        # for num in unique:
44        #     points=num*count[num]
45
46        #     if num==prev+1:
47        #         new_take=skip+points
48        #         new_skip=max(take,skip)
49        #     else:
50        #         best=max(take,skip)
51        #         new_take=best+points
52        #         new_skip=best
53        #     take=new_take
54        #     skip=new_skip
55        #     prev=num
56        # return max(take,skip)
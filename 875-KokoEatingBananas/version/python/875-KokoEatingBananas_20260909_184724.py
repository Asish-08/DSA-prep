# Last updated: 9/9/2026, 6:47:24 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        low,high=1,max(piles)
4        result=0
5        while low<=high:
6            hours=0
7            mid=(low+high)//2
8            for p in piles:
9                hours+=math.ceil(p/mid)
10            if hours<=h:
11                result=mid
12                high=mid-1
13            else:
14                low=mid+1
15        return result
16            
17            
18
19
20
21
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
33        # low,high=1,max(piles)
34        # result=high
35        # while low<=high:
36        #     mid=(low+high)//2
37        #     hours=0
38        #     for p in piles:
39        #         hours+=math.ceil(p/mid)
40        #     if hours<=h:
41        #         result=mid
42        #         high=mid-1
43        #     else:
44        #         low=mid+1
45
46        # return result
47
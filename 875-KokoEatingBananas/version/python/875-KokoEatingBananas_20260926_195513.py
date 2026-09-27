# Last updated: 9/26/2026, 7:55:13 PM
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
20        # low,high=1,max(piles)
21        # result=0
22        # while low<=high:
23        #     hours=0
24        #     mid=(low+high)//2
25        #     for p in piles:
26        #         hours+=math.ceil(p/mid)
27        #     if hours<=h:
28        #         result=mid
29        #         high=mid-1
30        #     else:
31        #         low=mid+1
32        # return result
33        
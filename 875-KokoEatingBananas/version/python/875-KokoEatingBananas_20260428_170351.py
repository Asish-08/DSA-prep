# Last updated: 4/28/2026, 5:03:51 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        low,high=1,max(piles)
4        result=high
5        while low<=high:
6            k=(low+high)//2
7            hours=0
8            for p in piles:
9                hours+=(p+k-1)//k
10            if hours<=h:
11                result=k
12                high=k-1
13            else:
14                low=k+1
15        return result
16            
17
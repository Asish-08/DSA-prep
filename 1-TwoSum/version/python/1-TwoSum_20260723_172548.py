# Last updated: 7/23/2026, 5:25:48 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        low,high=1,max(piles)
4        result=high
5        while low<=high:
6            k=(low+high)//2
7            hours=0
8            for p in piles:
9                hours+=math.ceil(p/k)
10            if hours <=h:
11                result=min(result,k)
12                high=k-1
13            else:
14                low=k+1
15        return result
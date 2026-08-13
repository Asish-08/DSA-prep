# Last updated: 8/12/2026, 7:26:11 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        low,high=max(weights),sum(weights)
4        result=0
5        while low<=high:
6            capacity=(low+high)//2
7            days_included=1
8            weight_capacity=0
9            for w in weights:
10                if weight_capacity+w>capacity:
11                    days_included+=1
12                    weight_capacity=w
13                else:
14                    weight_capacity+=w
15            if days_included<=days:
16                result=capacity
17                high=capacity-1
18            else:
19                low=capacity+1
20        return result
21
22
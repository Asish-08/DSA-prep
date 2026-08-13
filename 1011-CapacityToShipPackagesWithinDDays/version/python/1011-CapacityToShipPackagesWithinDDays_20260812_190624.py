# Last updated: 8/12/2026, 7:06:24 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        low,high=max(weights),sum(weights)
4        result=high
5        while low<=high:
6            capacity=(low+high)//2
7            current_weight=0
8            days_needed=1
9            for w in weights:
10                if current_weight+w > capacity:
11                    days_needed+=1
12                    current_weight=w
13                else:
14                    current_weight+=w
15            if days_needed<=days:
16                result=capacity
17                high=capacity-1
18            else:
19                low=capacity+1
20                
21        return result
22
23                
24
25
26
27
28        
# Last updated: 9/12/2026, 12:45:56 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        low,high=max(weights),sum(weights)
4        res=high
5
6        while low<=high:
7            currCapacity=(low+high)//2
8            currDays=1
9            weight_capacity=0
10            for w in weights:
11                if weight_capacity+w>currCapacity:
12                    currDays+=1
13                    weight_capacity=w
14                else:
15                    weight_capacity+=w
16            if currDays<=days:
17                res=currCapacity
18                high=currCapacity-1
19            else:
20                low=currCapacity+1
21        return res
22            
23                               
24
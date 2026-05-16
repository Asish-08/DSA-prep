# Last updated: 5/16/2026, 3:42:49 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas)< sum(cost):
4            return -1
5        start=0
6        tank=0
7
8        for i in range(len(gas)):
9            tank+=gas[i]-cost[i]
10            if tank<0:
11                start=i+1
12                tank=0
13        return start
14
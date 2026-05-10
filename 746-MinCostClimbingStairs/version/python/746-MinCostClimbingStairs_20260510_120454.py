# Last updated: 5/10/2026, 12:04:54 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n=len(cost)
4        prev2,prev1=cost[0],cost[1]
5        for i in range(2,n):
6            curr=cost[i]+min(prev2,prev1)
7            prev2,prev1=prev1,curr
8        return min(prev2,prev1)
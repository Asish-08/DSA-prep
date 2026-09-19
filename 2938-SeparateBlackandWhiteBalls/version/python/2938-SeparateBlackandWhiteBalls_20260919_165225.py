# Last updated: 9/19/2026, 4:52:25 PM
1class Solution:
2    def minimumSteps(self, s: str) -> int:
3        steps=0
4        ones=0
5
6        for c in s:
7            if c=='1':
8                ones+=1
9            else:
10                steps+=ones
11        return steps
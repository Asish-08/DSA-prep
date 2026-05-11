# Last updated: 5/10/2026, 7:36:15 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        ans=0
4        while n!=0:
5            ans+=1
6            n=n&(n-1)
7        return ans
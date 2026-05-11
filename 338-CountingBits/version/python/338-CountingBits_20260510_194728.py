# Last updated: 5/10/2026, 7:47:28 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans=[0]*(n+1)
4        def popcount(i):
5            count=0
6            while i!=0:
7                i=i&(i-1)
8                count+=1
9            return count
10        
11        for i in range(n+1):
12            ans[i]=popcount(i)
13        return ans
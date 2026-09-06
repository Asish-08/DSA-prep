# Last updated: 9/6/2026, 8:15:32 AM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        prices=[float('inf')]*n
4        prices[src]=0
5
6        for _ in range(k+1):
7            tmpPrices=prices.copy()
8
9            for s,d,p in flights:
10                if prices[s]==float('inf'):
11                    continue
12                if tmpPrices[d]> prices[s]+p:
13                    tmpPrices[d]=prices[s]+p
14            prices=tmpPrices
15        return -1 if prices[dst]==float('inf') else prices[dst]
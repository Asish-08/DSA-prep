# Last updated: 9/27/2026, 3:38:02 PM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        prices=[float('inf')]*n
4        prices[src]=0
5
6        for _ in range(k+1):
7            tmpPrices=prices.copy()
8            for s,d,p in flights:
9                if tmpPrices[s]==float('inf'):
10                    continue
11                if tmpPrices[d]>prices[s]+p:
12                    tmpPrices[d]=prices[s]+p
13            prices=tmpPrices
14        return -1 if tmpPrices[dst]==float('inf') else prices[dst]
15                    
16
17
18        # prices=[float('inf')]*n
19        # prices[src]=0
20
21        # for _ in range(k+1):
22        #     tmpPrices=prices.copy()
23
24        #     for s,d,p in flights:
25        #         if prices[s]==float('inf')
26        #             continue
27        #         if tmpPrices[d]> prices[s]+p:
28        #             tmpPrices[d]=prices[s]+p
29        #     prices=tmpPrices
30        # return -1 if prices[dst]==float('inf') else prices[dst]
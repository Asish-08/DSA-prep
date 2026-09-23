# Last updated: 9/22/2026, 8:12:51 PM
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
11                if tmpPrices[d]> prices[s]+p:
12                    tmpPrices[d]=prices[s]+p
13            prices=tmpPrices
14        return -1 if prices[dst]==float('inf') else prices[dst]
15                    
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31        # prices=[float('inf')]*n
32        # prices[src]=0
33
34        # for _ in range(k+1):
35        #     tmpPrices=prices.copy()
36
37        #     for s,d,p in flights:
38        #         if prices[s]==float('inf')
39        #             continue
40        #         if tmpPrices[d]> prices[s]+p:
41        #             tmpPrices[d]=prices[s]+p
42        #     prices=tmpPrices
43        # return -1 if prices[dst]==float('inf') else prices[dst]
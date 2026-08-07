# Last updated: 8/6/2026, 10:57:15 PM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack=[]
5
6    def next(self, price: int) -> int:
7        ans=1
8        while self.stack and price >= self.stack[-1][0]:
9            ans+=self.stack.pop()[1]
10        self.stack.append([price,ans])
11        return ans
12
13
14# Your StockSpanner object will be instantiated and called as such:
15# obj = StockSpanner()
16# param_1 = obj.next(price)
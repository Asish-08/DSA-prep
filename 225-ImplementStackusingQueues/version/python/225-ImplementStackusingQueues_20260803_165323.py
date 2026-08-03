# Last updated: 8/3/2026, 4:53:23 PM
1from collections import deque
2class MyStack:
3
4    def __init__(self):
5        self.q=deque()
6
7    def push(self, x: int) -> None:
8        self.q.append(x)
9        for _ in range(len(self.q)-1):
10            self.q.append(self.q.popleft())
11
12    def pop(self) -> int:
13        return self.q.popleft()
14
15    def top(self) -> int:
16        return self.q[0]
17        
18
19    def empty(self) -> bool:
20        return len(self.q)==0
21        
22
23
24# Your MyStack object will be instantiated and called as such:
25# obj = MyStack()
26# obj.push(x)
27# param_2 = obj.pop()
28# param_3 = obj.top()
29# param_4 = obj.empty()
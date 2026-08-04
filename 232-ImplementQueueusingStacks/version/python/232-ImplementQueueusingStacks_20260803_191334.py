# Last updated: 8/3/2026, 7:13:34 PM
1class MyQueue:
2
3    def __init__(self):
4        self.instack=[]
5        self.outstack=[]
6
7    def push(self, x: int) -> None:
8        return self.instack.append(x)
9
10    def pop(self) -> int:
11        if not self.outstack:
12            while self.instack:
13                self.outstack.append(self.instack.pop())
14        return self.outstack.pop()
15
16    def peek(self) -> int:
17        if not self.outstack:
18            while self.instack:
19                self.outstack.append(self.instack.pop())
20        return self.outstack[-1]
21        
22
23    def empty(self) -> bool:
24        return not self.instack and not self.outstack
25
26
27# Your MyQueue object will be instantiated and called as such:
28# obj = MyQueue()
29# obj.push(x)
30# param_2 = obj.pop()
31# param_3 = obj.peek()
32# param_4 = obj.empty()
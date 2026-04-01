# Last updated: 4/1/2026, 3:52:08 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pair=[[p,s] for p,s in zip(position,speed)]
4        stack=[]
5        
6        for p,s in sorted(pair)[::-1]: #reverse order
7            stack.append((target-p)/s)
8            if len(stack)>=2 and stack[-1]<=stack[-2]: #time of the stack[-1] is less than stack[-2]
9                stack.pop()
10        return len(stack)
11
12        
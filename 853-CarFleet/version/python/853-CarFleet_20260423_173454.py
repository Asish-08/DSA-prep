# Last updated: 4/23/2026, 5:34:54 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pair=[[p,s] for p,s in zip(position,speed)]
4        stack=[]
5
6        for p,s in sorted(pair)[::-1]:
7            val=(target-p)/s
8            stack.append(val)
9            if len(stack)>=2 and stack[-1]<=stack[-2]:
10                stack.pop()
11        return len(stack)
12
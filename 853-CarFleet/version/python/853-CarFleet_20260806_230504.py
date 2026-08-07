# Last updated: 8/6/2026, 11:05:04 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pair=[[p,s] for p,s in zip(position,speed)]
4        fleet_stack=[]
5        for p,s in sorted(pair)[::-1]:
6            time=(target-p)/s
7            fleet_stack.append(time)
8            if len(fleet_stack)>=2 and fleet_stack[-1]<=fleet_stack[-2]:
9                fleet_stack.pop()
10        return len(fleet_stack)
11
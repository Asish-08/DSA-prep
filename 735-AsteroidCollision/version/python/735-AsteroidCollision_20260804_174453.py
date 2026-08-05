# Last updated: 8/4/2026, 5:44:53 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        res=[]
4        stack=[]
5        for i in asteroids:
6            if i >0:
7                stack.append(i)
8            else:
9                while stack and stack[-1]<abs(i):
10                    stack.pop()
11                if len(stack)==0:
12                    res.append(i)
13                else:
14                    if stack[-1]==abs(i):
15                        stack.pop()
16        res+=stack
17        return res
18    
19    
20    
21
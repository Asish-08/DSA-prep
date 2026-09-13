# Last updated: 9/12/2026, 7:47:25 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        res=[]
4        stack=[]
5        for i in asteroids:
6            if i>0:
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
22
23
24        # res=[]
25        # stack=[]
26        # for i in asteroids:
27        #     if i >0:
28        #         stack.append(i)
29        #     else:
30        #         while stack and stack[-1]<abs(i):
31        #             stack.pop()
32        #         if len(stack)==0:
33        #             res.append(i)
34        #         else:
35        #             if stack[-1]==abs(i):
36        #                 stack.pop()
37        # res+=stack
38        # return res
39    
40    
41    
42
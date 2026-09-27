# Last updated: 9/27/2026, 6:48:46 AM
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
23        # res=[]
24        # stack=[]
25        # for i in asteroids:
26        #     if i>0:
27        #         stack.append(i)
28        #     else:
29        #         while stack and stack[-1]<abs(i):
30        #             stack.pop()
31        #         if len(stack)==0:
32        #             res.append(i)
33        #         else:
34        #             if stack[-1]==abs(i):
35        #                 stack.pop()
36        # res+=stack
37        # return res
38
39
40
41
42
43
44        # res=[]
45        # stack=[]
46        # for i in asteroids:
47        #     if i >0:
48        #         stack.append(i)
49        #     else:
50        #         while stack and stack[-1]<abs(i):
51        #             stack.pop()
52        #         if len(stack)==0:
53        #             res.append(i)
54        #         else:
55        #             if stack[-1]==abs(i):
56        #                 stack.pop()
57        # res+=stack
58        # return res
59    
60    
61    
62
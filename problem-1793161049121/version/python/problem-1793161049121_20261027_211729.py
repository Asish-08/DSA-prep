# Last updated: 10/27/2026, 9:17:29 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        open_stack=[]
4        star_stack=[]
5
6        for i,c in enumerate(s):
7            if c=='(':
8                open_stack.append(i)
9
10            elif c=='*':
11                star_stack.append(i)
12            
13            else:
14                if open_stack:
15                    open_stack.pop()
16                elif star_stack:
17                    star_stack.pop()
18                else:
19                    return False
20        while open_stack and star_stack:
21            if open_stack[-1] > star_stack[-1]:
22                return False
23            open_stack.pop()
24            star_stack.pop()
25
26        return len(open_stack)==0
27        
28            
29            
30
31
32
33        
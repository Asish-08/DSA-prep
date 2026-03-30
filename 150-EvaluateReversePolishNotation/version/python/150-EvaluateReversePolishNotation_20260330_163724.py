# Last updated: 3/30/2026, 4:37:24 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack=[]
4        for c in tokens:
5            if c not in ['+','-','*','/']:
6                stack.append(int(c))
7            else:
8                b=int(stack.pop())
9                a=int(stack.pop())
10                if c=='+':
11                    val=a+b
12                    stack.append(val)
13                if c=='-':
14                    val=(a-b)
15                    stack.append(val)
16                if c=='*':
17                    val=(a*b)
18                    stack.append(val)
19                if c=='/':
20                    val=(a/b)
21                    stack.append(val)
22        return int(stack[-1])
23
# Last updated: 9/5/2026, 5:49:02 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res=[]
4        stack=[]
5
6        def backtrack(openN,closedN):
7            if openN==n and closedN==n:
8                res.append(''.join(stack))
9                return
10            if openN<n:
11                stack.append('(')
12                backtrack(openN+1,closedN)
13                stack.pop()
14            if closedN<openN:
15                stack.append(')')
16                backtrack(openN,closedN+1)
17                stack.pop()
18        backtrack(0,0)
19        return res
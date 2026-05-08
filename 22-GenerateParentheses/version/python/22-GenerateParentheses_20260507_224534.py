# Last updated: 5/7/2026, 10:45:34 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res=[]
4        stack=[]
5        def backtrack(openN,closedN):
6            if openN==n and closedN==n:
7                res.append(''.join(stack))
8                return
9            if openN<n:
10                stack.append('(')
11                backtrack(openN+1,closedN)
12                stack.pop()
13            if openN > closedN:
14                stack.append(')')
15                backtrack(openN,closedN+1)
16                stack.pop()
17        backtrack(0,0)
18        return res
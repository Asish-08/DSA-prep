# Last updated: 8/6/2026, 11:11:16 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack=[]
4        for s in path.split('/'):
5            if s =="..":
6                if stack:
7                    stack.pop()
8            elif s=="." or not s:
9                continue
10            else:
11                stack.append(s)
12        return "/"+"/".join(stack)
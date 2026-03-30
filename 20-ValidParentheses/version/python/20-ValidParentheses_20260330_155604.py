# Last updated: 3/30/2026, 3:56:04 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        h_map={')':'(',']':'[','}':'{'}
4        stack=[]
5        for c in s:
6            if c in h_map:
7                if stack and h_map[c]==stack[-1]:
8                    stack.pop()
9                else:
10                    return False
11            else:
12                stack+=c
13        return True if not stack else False
# Last updated: 7/31/2026, 8:44:28 PM
1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        stack=[]
4        for op in operations:
5            if op=="+":
6                stack.append(stack[-1]+stack[-2])
7            elif op=="C":
8                stack.pop()
9            elif op=="D":
10                stack.append(stack[-1]*2)
11            else:
12                stack.append(int(op))
13        return sum(stack)
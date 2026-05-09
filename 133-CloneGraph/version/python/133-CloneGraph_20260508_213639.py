# Last updated: 5/8/2026, 9:36:39 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        oldtonew={}
13        
14        def dfs(node):
15            if node in oldtonew:
16                return oldtonew[node]
17            copy=Node(node.val)
18            oldtonew[node]=copy
19            for nei in node.neighbors:
20                copy.neighbors.append(dfs(nei))
21            return copy
22        
23        return dfs(node) if node else None
# Last updated: 5/6/2026, 8:22:02 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        def dfs(node,maxVal):
10            if not node:
11                return 0
12            res=1 if node.val>=maxVal else 0
13            maxVal=max(maxVal,node.val)
14            res+=dfs(node.left,maxVal)
15            res+=dfs(node.right,maxVal)
16            return res
17        return dfs(root,root.val)
18
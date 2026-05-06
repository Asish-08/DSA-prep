# Last updated: 5/6/2026, 4:15:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        self.max_diameter=0
10        def dfs(node):
11            if not node:
12                return 0
13            left=dfs(node.left)
14            right=dfs(node.right)
15            self.max_diameter=max(self.max_diameter, left+right)
16            return 1+max(left,right)
17        dfs(root)
18        return self.max_diameter
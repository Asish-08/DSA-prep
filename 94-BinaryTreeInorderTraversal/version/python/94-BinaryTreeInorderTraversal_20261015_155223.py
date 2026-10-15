# Last updated: 10/15/2026, 3:52:23 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
9        def helper(root,res):
10            if root is not None:
11                helper(root.left,res)
12                res.append(root.val)
13                helper(root.right,res)
14        res=[]
15        helper(root,res)
16        return res
17
18        
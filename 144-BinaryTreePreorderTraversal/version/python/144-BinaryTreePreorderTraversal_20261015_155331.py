# Last updated: 10/15/2026, 3:53:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
9        def helper(root,res):
10            if root:
11                res.append(root.val)
12                helper(root.left,res)
13                helper(root.right,res)
14        res=[]
15        helper(root,res)
16        return res
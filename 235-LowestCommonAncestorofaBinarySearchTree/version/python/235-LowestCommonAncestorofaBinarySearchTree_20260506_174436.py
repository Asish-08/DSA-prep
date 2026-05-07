# Last updated: 5/6/2026, 5:44:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        curr=root
11        while root:
12            if p.val<curr.val and q.val<curr.val:
13                curr=curr.left
14            elif p.val>curr.val and q.val>curr.val:
15                curr=curr.right
16            else:
17                return curr
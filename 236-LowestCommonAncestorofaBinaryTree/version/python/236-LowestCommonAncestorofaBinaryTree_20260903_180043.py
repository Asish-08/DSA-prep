# Last updated: 9/3/2026, 6:00:43 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root or root==p or root==q:
11            return root
12        left=self.lowestCommonAncestor(root.left,p,q)
13        right=self.lowestCommonAncestor(root.right,p,q)
14
15        if left and right:
16            return root
17        return left if left else right
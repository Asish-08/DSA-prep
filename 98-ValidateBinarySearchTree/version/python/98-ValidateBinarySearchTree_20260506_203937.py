# Last updated: 5/6/2026, 8:39:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        def validTree(node,left,right):
10            if not node:
11                return True
12            if not(left<node.val<right):
13                return False
14            return (validTree(node.left,left,node.val) and validTree(node.right,node.val,right))
15        return validTree(root,float('-inf'),float('inf'))
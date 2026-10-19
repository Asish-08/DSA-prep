# Last updated: 10/19/2026, 4:28:15 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
9        if not root:
10            return TreeNode(val)
11        if root.val < val:
12            root.right=self.insertIntoBST(root.right,val)
13        else:
14            root.left=self.insertIntoBST(root.left,val)
15        return root
16
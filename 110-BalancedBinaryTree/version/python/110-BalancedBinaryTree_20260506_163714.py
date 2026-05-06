# Last updated: 5/6/2026, 4:37:14 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def height(self,root:TreeNode)->int:
9        if not root:
10            return -1
11        return 1+max(self.height(root.left),self.height(root.right))
12
13    def isBalanced(self, root: Optional[TreeNode]) -> bool:
14        if not root:
15            return True
16        if abs(self.height(root.left)-self.height(root.right))>1:
17            return False
18        else:
19            return self.isBalanced(root.left) and self.isBalanced(root.right)
20        
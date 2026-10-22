# Last updated: 10/22/2026, 4:51:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
9        if not root:
10            return None
11        root.left=self.removeLeafNodes(root.left,target)
12        root.right=self.removeLeafNodes(root.right,target)
13        if not root.left and not root.right and root.val==target:
14            return None
15        return root
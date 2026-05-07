# Last updated: 5/7/2026, 12:23:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        self.result=None
10        self.count=0
11        def inorder(node):
12            if not node or (self.result is not None):
13                return 
14            inorder(node.left)
15            self.count+=1
16            if self.count==k:
17                self.result=node.val
18                return
19            inorder(node.right)
20        inorder(root)
21        return self.result
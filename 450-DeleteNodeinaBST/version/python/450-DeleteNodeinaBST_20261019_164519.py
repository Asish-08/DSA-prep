# Last updated: 10/19/2026, 4:45:19 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
9        if not root:
10            return 
11        if key < root.val:
12            root.left=self.deleteNode(root.left,key)
13        elif key > root.val:
14            root.right=self.deleteNode(root.right,key)
15        else:
16            if not root.left:
17                return root.right
18            elif not root.right:
19                return root.left
20            else:
21                min_node=self.getMin(root.right)
22                root.val=min_node.val
23                root.right=self.deleteNode(root.right,min_node.val)
24        return root
25        
26    def getMin(self,node):
27        while node.left:
28            node=node.left
29        return node
# Last updated: 5/6/2026, 5:28:32 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        def sametree(p,q):
10            if not p and not q:
11                return True
12            if not p or not q or p.val!=q.val:
13                return False
14            return sametree(p.left,q.left) and sametree(p.right,q.right)
15        
16        if not subRoot:
17            return True
18        if not root:
19            return False
20        if sametree(root,subRoot):
21            return True
22        
23        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
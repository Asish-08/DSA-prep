# Last updated: 9/3/2026, 8:24:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        res=[root.val]
10
11        def dfs(root):
12            if not root:
13                return 0
14            leftval=dfs(root.left)
15            rightval=dfs(root.right)
16            leftval=max(leftval,0)
17            rightval=max(rightval,0)
18
19            #including the split
20            res[0]=max(res[0], root.val+leftval+rightval)
21        
22            return root.val+max(leftval,rightval) 
23        dfs(root)
24
25        return res[0]
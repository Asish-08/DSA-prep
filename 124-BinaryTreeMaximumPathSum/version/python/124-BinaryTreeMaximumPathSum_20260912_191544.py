# Last updated: 9/12/2026, 7:15:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        res=[root.val]
10        def dfs(root):
11            if not root:
12                return 0
13            leftval=dfs(root.left)
14            rightval=dfs(root.right)
15            leftval=max(leftval,0)
16            rightval=max(rightval,0)
17
18            #considering the split
19            res[0]=max(res[0],root.val+leftval+rightval)
20
21            return root.val+max(leftval,rightval)
22        dfs(root)
23        return res[0]
24
25
26
27
28
29
30
31        # res=[root.val]
32
33        # def dfs(root):
34        #     if not root:
35        #         return 0
36        #     leftval=dfs(root.left)
37        #     rightval=dfs(root.right)
38        #     leftval=max(leftval,0)
39        #     rightval=max(rightval,0)
40
41        #     #including the split
42        #     res[0]=max(res[0], root.val+leftval+rightval)
43        
44        #     return root.val+max(leftval,rightval) 
45        # dfs(root)
46
47        # return res[0]
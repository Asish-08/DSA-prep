# Last updated: 9/27/2026, 6:37:08 AM
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
13            left_val=dfs(root.left)
14            right_val=dfs(root.right)
15            left_max=max(left_val,0)
16            right_max=max(right_val,0)
17
18            res[0]=max(res[0],root.val+left_max+right_max)
19            return root.val+max(left_max,right_max)
20        dfs(root)
21
22        return res[0]
23
24
25
26
27
28
29        # res=[root.val]
30        # def dfs(root):
31        #     if not root:
32        #         return 0
33        #     leftval=dfs(root.left)
34        #     rightval=dfs(root.right)
35        #     leftval=max(leftval,0)
36        #     rightval=max(rightval,0)
37
38        #     #considering the split
39        #     res[0]=max(res[0],root.val+leftval+rightval)
40
41        #     return root.val+max(leftval,rightval)
42        # dfs(root)
43        # return res[0]
44
45
46
47
48
49
50
51        # res=[root.val]
52
53        # def dfs(root):
54        #     if not root:
55        #         return 0
56        #     leftval=dfs(root.left)
57        #     rightval=dfs(root.right)
58        #     leftval=max(leftval,0)
59        #     rightval=max(rightval,0)
60
61        #     #including the split
62        #     res[0]=max(res[0], root.val+leftval+rightval)
63        
64        #     return root.val+max(leftval,rightval) 
65        # dfs(root)
66
67        # return res[0]
# Last updated: 9/3/2026, 7:59:21 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        #raturn pair: [withroot, withoutroot]
10        def dfs(root):
11            if not root:
12                return [0,0]
13            leftval=dfs(root.left)
14            rightval=dfs(root.right)
15            withroot=root.val+leftval[1]+rightval[1]
16            withoutroot=max(leftval)+max(rightval)
17            return [withroot, withoutroot]
18
19        return max(dfs(root))
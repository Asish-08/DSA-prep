# Last updated: 9/12/2026, 5:26:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        #propagating the values from bottom level to the top
10        #return pair: [withroot, withoutroot]
11        # def dfs(root):
12        #     if not root:
13        #         return [0,0]
14        #     leftval=dfs(root.left) 
15        #     rightval=dfs(root.right)
16        #     withroot=root.val+leftval[1]+rightval[1]
17        #     withoutroot=max(leftval)+max(rightval)
18        #     return [withroot, withoutroot]
19
20        # return max(dfs(root))
21        def dfs(root):
22            if not root:
23                return [0,0]
24            #making the withroot and without root values
25            leftval=dfs(root.left)
26            rightval=dfs(root.right)
27            withroot=root.val+leftval[1]+rightval[1]
28            withoutroot=max(leftval)+max(rightval)
29            return [withroot,withoutroot]
30        return max(dfs(root))
# Last updated: 9/3/2026, 10:17:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        #recursive DFS
10        # if not root:
11        #     return 0
12        # left_height=self.maxDepth(root.left)
13        # right_height=self.maxDepth(root.right)
14        # return 1+max(left_height,right_height)
15
16        #BFS
17        # if not root:
18        #     return 0
19        # q=deque([root])
20        # level=0
21        # while q:
22        #     for i in range(len(q)):
23        #         node=q.popleft()
24        #         if node.left:
25        #             q.append(node.left)
26        #         if node.right:
27        #             q.append(node.right)
28        #     level+=1
29        # return level
30
31        #iterative DFS
32        if not root:
33            return 0
34        left=self.maxDepth(root.left)
35        right=self.maxDepth(root.right)
36        height=max(left,right)
37        return 1+height
38
39
40            
41
# Last updated: 5/6/2026, 7:26:23 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        res=[]
10        if not root:
11            return []
12        q=deque([root])
13        res=[]
14        while q:
15            level_size=len(q)
16            for i in range(len(q)):
17                node=q.popleft()
18                if i==level_size-1:
19                    res.append(node.val)
20                if node.left:
21                    q.append(node.left)
22                if node.right:
23                    q.append(node.right)
24        return res
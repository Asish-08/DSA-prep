# Last updated: 5/6/2026, 6:49:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        res=[]
12        q=deque([root])
13        while q:
14            level=[]
15            for _ in range(len(q)):
16                node=q.popleft()
17                level.append(node.val)
18                if node.left:
19                    q.append(node.left)
20                if node.right:
21                    q.append(node.right)
22            res.append(level)
23        return res
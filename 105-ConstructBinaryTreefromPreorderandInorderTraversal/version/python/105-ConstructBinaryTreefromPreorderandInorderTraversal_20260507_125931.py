# Last updated: 5/7/2026, 12:59:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.hashmap={}
        for i in range(len(inorder)):
            self.hashmap[inorder[i]]=i
        
        return self.build(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
    
    def build(self,preorder,prestart,preend,inorder,instart,inend):
        if prestart>preend:
            return

        root=TreeNode(preorder[prestart])
        index=self.hashmap[root.val]
        leftsize=index-instart

        root.left=self.build(preorder,prestart+1,prestart+leftsize,inorder,instart,index-1)
        root.right=self.build(preorder,prestart+leftsize+1,preend,inorder,index+1,inend)
        return root




            
# Last updated: 5/5/2026, 5:04:36 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy=ListNode(0,head)
9        left=dummy
10        right=head
11        #finding the node to be deleted
12        for _ in range(n):
13            right=right.next
14        
15        #constructing the LL
16        while right:    #breaks when right reaches none and left reaches prev node-to-delete
17            left=left.next
18            right=right.next
19        left.next=left.next.next
20        return dummy.next
21
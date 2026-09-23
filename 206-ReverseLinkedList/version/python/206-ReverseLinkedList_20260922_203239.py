# Last updated: 9/22/2026, 8:32:39 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev=None
9        curr=head
10
11        while curr:
12            nxt=curr.next
13            curr.next=prev
14            prev=curr
15            curr=nxt
16        return prev    
17
18
19
20
21        # prev=None
22        # curr=head
23
24        # while curr:
25        #     nxt=curr.next
26        #     curr.next=prev
27        #     prev=curr
28        #     curr=nxt
29        # return prev
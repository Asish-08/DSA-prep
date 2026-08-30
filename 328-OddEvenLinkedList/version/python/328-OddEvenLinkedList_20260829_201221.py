# Last updated: 8/29/2026, 8:12:21 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        evens=ListNode(0)
9        odds=ListNode(0)
10        evensHead=evens
11        oddsHead=odds
12        isOdd=True
13
14        while head:
15            if isOdd:
16                odds.next=head
17                odds=odds.next
18            else:
19                evens.next=head
20                evens=evens.next
21            head=head.next
22            isOdd=not isOdd
23        evens.next=None
24        odds.next=evensHead.next
25        return oddsHead.next
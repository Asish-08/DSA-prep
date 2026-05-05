# Last updated: 5/4/2026, 5:58:12 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy=ListNode
9        current=dummy
10        l1,l2=list1,list2
11        while l1 and l2:
12            if l1.val<l2.val:
13                current.next=l1
14                l1=l1.next
15            else:
16                current.next=l2
17                l2=l2.next
18            current=current.next
19        current.next=l1 if l1 else l2
20        return dummy.next
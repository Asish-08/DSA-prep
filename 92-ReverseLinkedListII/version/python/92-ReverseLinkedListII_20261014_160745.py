# Last updated: 10/14/2026, 4:07:45 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
8        if not head or left==right:
9            return head
10        dummy=ListNode(0,head)
11        prev=dummy
12
13        for _ in range(left-1):
14            prev=prev.next
15
16        # Reverse the sublist using repeated front insertion
17        curr=prev.next
18        for _ in range(right-left):
19            node=curr.next
20            curr.next=node.next
21            node.next=prev.next
22            prev.next=node
23        return dummy.next
24        
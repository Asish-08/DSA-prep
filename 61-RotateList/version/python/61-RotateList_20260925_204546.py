# Last updated: 9/25/2026, 8:45:46 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
8        if not head:
9            return head
10        length=1
11        tail=head
12
13        while tail.next:
14            tail=tail.next
15            length+=1
16        k=k%length
17
18        if k==0:
19            return head
20        
21        cur=head
22        for i in range(length-k-1):
23            cur=cur.next
24        new_head=cur.next
25        cur.next=None
26        tail.next=head
27        return new_head
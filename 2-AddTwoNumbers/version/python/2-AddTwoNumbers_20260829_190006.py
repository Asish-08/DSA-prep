# Last updated: 8/29/2026, 7:00:06 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        carry=0
9        res=ListNode(0)
10        curr=res
11
12        while l1 or  l2 or  carry:
13            l1_val=l1.val if l1 else 0
14            l2_val= l2.val if l2 else 0
15            total=l1_val+l2_val+carry
16
17            carry=total//10
18            digit=total%10
19
20            new_node=ListNode(digit)
21            curr.next=new_node
22            curr=curr.next
23
24            if l1:
25                l1=l1.next
26            if l2:
27                l2=l2.next
28        return res.next
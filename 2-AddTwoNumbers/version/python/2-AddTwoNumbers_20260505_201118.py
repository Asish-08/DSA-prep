# Last updated: 5/5/2026, 8:11:18 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        res=ListNode(0)
9        carry=0
10        curr=res
11        while l1!= None or l2 != None or carry!=0:
12            l1_val=l1.val if l1 else 0
13            l2_val=l2.val if l2 else 0
14            total=(l1_val+l2_val+carry)
15            carry=(total)//10
16            digit=total%10
17            
18            new_node=ListNode(digit)
19            curr.next=new_node
20            curr=curr.next
21
22            l1=l1.next if l1 else None
23            l2=l2.next if l2 else None
24        return res.next
25
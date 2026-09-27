# Last updated: 9/26/2026, 8:24:11 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        carry=0
9        res=ListNode(0)
10        cur=res
11        while l1 or l2 or carry:
12            l1_val=l1.val if l1 else 0
13            l2_val=l2.val if l2 else 0
14            total=l1_val+l2_val+carry
15
16            carry=total//10
17            digit=total%10
18
19            new_node=ListNode(digit)
20            cur.next=new_node
21            cur=cur.next
22
23            if l1:
24                l1=l1.next
25            if l2:
26                l2=l2.next
27        return res.next
28
29
30
31
32
33
34
35        # carry=0
36        # res=ListNode(0)
37        # curr=res
38
39        # while l1 or  l2 or  carry:
40        #     l1_val=l1.val if l1 else 0
41        #     l2_val= l2.val if l2 else 0
42        #     total=l1_val+l2_val+carry
43
44        #     carry=total//10
45        #     digit=total%10
46
47        #     new_node=ListNode(digit)
48        #     curr.next=new_node
49        #     curr=curr.next
50
51        #     if l1:
52        #         l1=l1.next
53        #     if l2:
54        #         l2=l2.next
55        # return res.next
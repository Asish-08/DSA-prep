# Last updated: 9/27/2026, 7:20:57 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        nodes_seen=set()
10        curr=head
11        while curr:
12            if curr and curr in nodes_seen:
13                return True
14            nodes_seen.add(curr)
15            curr=curr.next
16        return False
17
18
19
20        # nodes_seen=set()
21        # curr=head
22        # while curr:
23        #     if curr in nodes_seen:
24        #         return True
25        #     nodes_seen.add(curr)
26        #     curr=curr.next
27        # return False
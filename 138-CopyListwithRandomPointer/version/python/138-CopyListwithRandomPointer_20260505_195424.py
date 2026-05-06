# Last updated: 5/5/2026, 7:54:24 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        old_to_copy={None:None} #if the LL node is at end, it should point to Null node
13        curr=head
14
15        #creating the copy values for the LL
16        while curr:
17            old_to_copy[curr]=Node(curr.val)
18            curr=curr.next
19        
20        #linking the nodes with the next and random pointers
21        curr=head
22        while curr:
23            copy=old_to_copy[curr]
24            copy.next=old_to_copy[curr.next]
25            copy.random=old_to_copy[curr.random]
26            curr=curr.next
27        return old_to_copy[head]
28        
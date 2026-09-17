"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # original node -> copied node
        mapping = {}

        # Pass 1: create a new node for every original node
        curr = head

        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: connect next and random pointers
        curr = head

        while curr:
            copy_node = mapping[curr]

            if curr.next:
                copy_node.next = mapping[curr.next]
            else:
                copy_node.next = None

            if curr.random:
                copy_node.random = mapping[curr.random]
            else:
                copy_node.random = None

            curr = curr.next

        return mapping[head]
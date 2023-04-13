# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Implement the Solution class:

# Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random 
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.length = 0
        self.head = head
        node = head
        while node.next != None:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        node = self.head
        for i in range(random.randint(0, self.length)):
            node = node.next
        return node.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
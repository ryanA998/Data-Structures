#LeetCode Problem 237: Deleting a Node from a Linked List 
#Author: Ryan Arendt
#Verified: 10/27/2020 

#LeetCode Problem 237: 
#Description: Deleting a Node from a Linked List 
    # Write a function to delete a node in a singly-linked list.
    # You will not be given access to the head of the list, instead you 
    # will be given access to the node to be deleted directly.
    # It is guaranteed that the node to be deleted is not a tail node in the list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val 
        node.next = node.next.next



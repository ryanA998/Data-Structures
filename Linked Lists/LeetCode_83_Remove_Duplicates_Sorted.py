
#LeetCode Problem 83: Remove Duplicates from a Sorted Linked List
#Author: Ryan Arendt
#Verified: 10/27/2020 

#Description: 
#Given a sorted linked list, delete all duplicates such that each element appear only once.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head): 
        
        #If the linked list is empty or it just contains the head: just return the head
        if head == None or head.next == None:
            return head 

        cur_node = head 

        while cur_node.next != None:   
            #If the current value and next value are the same
            if cur_node.val == cur_node.next.val: 
                cur_node.next = cur_node.next.next
                
                if cur_node == None:
                    cur_node = cur_node.next.next 
            #The current value and the next value are not the same: 
            #just increment the list.
            else: 
                cur_node = cur_node.next
        
        return head


def disp_list(l): 
    while l: 
        print(l.val)
        l=l.next

# n_1 = ListNode(1)
# n_2 = ListNode(1)
# n_3 = ListNode(2)
# # n_4 = ListNode(3)
# # n_5 = ListNode(3)

# n_1.next = n_2
# n_2.next = n_3 
# # n_3.next = n_4 
# # n_4.next = n_5 

# #disp_list(n_1)
# s = Solution.deleteDuplicates(n_1, n_1)
# disp_list(n_1)
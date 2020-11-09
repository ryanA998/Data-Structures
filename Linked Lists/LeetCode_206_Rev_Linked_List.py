#LeetCode: Problem 206
#Author: Ryan Arendt
#Verified: 10/27/2020 

#Description: Reverse a Linked List 
# Problem: Reverse a singly linked list.
# Example:
#       Input: 1->2->3->4->5->NULL
#       Output: 5->4->3->2->1->NULL

class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


class Solution:
    def reverseList(self, head):
        
        cur_head = head 
        cur_node = head 

        #If the head is empty: just return the empty head
        if head == None: 
            return head
        
        #Else: the linked list at least contains one node
        else:
            #Iterate through the linked list
            while cur_node.next != None: 
                temp_head = cur_node.next 
                cur_node.next = cur_node.next.next 
                temp_head.next = cur_head
                cur_head = temp_head 

        return cur_head


#Temporary helper function that displays all of 
#the nodes in the link list: from head->tail.
def disp_list(l): 
    while l:
        print(l.val)
        l = l.next



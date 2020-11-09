#Representation of a Linked list with a built in cursor 
#Author: Ryan Arendt
#Adapted from: IIT CS-331 Data Stuctures & Algorithems Lecture

""" Here a "cursor" is added our basic implementation of a Linked List. The cursor allows us to keep a spot in the
    linked list and insert or delete items at that spot vs. always traversing through the Linked List. 
"""

class LinkedList: 
    class Node: 
        def __init__(self, val, prior=None, next=None): 
            self.val = val 
            self.prior = prior 
            self.next = next 
    
    def __init__(self): 
        self.head = self.cursor = LinkedList.Node(None)
        self.head.prior = self.head.next = self.head 
        self.count = 0

    def append(self, value): 
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        n.prior.next = n.next.prior = n 
        self.count += 1 

    def cursor_set(self, idx):
        #What does it mean to set a cursor? Remember a particular position
        #for future inserts and deletions. 
        self.cursor = self.head.next 
        for _ in range(idx): 
            n = n.next

        self.cursor = n

    def cursor_insert(self, x):
        #What does insert a cursor mean? Insert a thing right after the
        #current cursor positon .
        p = self.cursor
        n = LinkedList.Node(x, prior=p, next=p.next)
        p.next.prior = n 
        p.next = n 
        self.count += 1


    def cursor_delete(self):
        #What does cursor delete? Delete the thing imediately after the cursor 
        to_del = self.cursor.next 
        #Want to make sure that you dont delete the sentinal head 
        #Take the references around them and forget me 
        to_del.next.prior = to_del.prior 
        to_del.prior.next = to_del.next
        self.count -= 1

    def __len__(self):
        return self.count 

    def __iter__(self): 
        n = self.head.next 
        while n is not self.head: 
            yield n.val 
            n = n.next
#Two different implementation of a Linked List in Python
#Author: Ryan Arendt
#Adapted from: IIT CS-331 Data Stuctures & Algorithems Lecture

""" Here two different versions of a Linked List are given. LinkedList2 gives a 'tail' as an additional
    attribute whereas LinkeList gives a more 'vanila' implementation using just a 'head' attribute.
"""

class LinkedList2: 
    class Node: 
        def __init__(self, val, next=None):
            self.val = val
            self.next= next 
    def __init__(self): 
        self.head = None 
        self.tail = None
        self.count = 0

    def prepend(self, value): 
        self.head = LinkedList2.Node(value, self.head)
        if not self.tail: 
            self.tail = self.head 

        self.count += 1

    def append(self, value): 
        if not self.head: 
            self.prepend(value)

        else: 
            l = LinkedList2.Node(value)
            self.tail.next = l
            self.tail = l 
            self.count += 1


class LinkedList: 
    class Node: 
        def __init__(self, val, next=None):
            self.val = val
            self.next= next 

    def __init__(self): 
        self.head = None 
        self.count = 0

    def prepend(self, val):
        self.head = LinkedList.Node(val, self.head)
        self.count += 1

    def append(self, val): 
        #Trival case: the list is empty
        if len(self) == 0:
            self.prepend(val)
        #The note at the end needs to reference to the new node
        else: 
            #Need to traverse the entire list: and find the node
            #whos next node is None: refer to the new node 
            n = self.head 
            while n.next: 
                n = n.next 

            #Now n referrs to the last node 
            n.next = LinkedList.Node(val)
            self.count += 1

        
    def __len__(self):
        return self.count
    
    def __iter__(self):
        n = self.head 
        while n:
            yield n.val
            n = n.next

    def __repr__(self):
        
        return '['+','.join(str(x) for x in self) +']'

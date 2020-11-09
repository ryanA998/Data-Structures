#Implementation of a Doubly Linked List in Python
#Author: Ryan Arendt
#Adapted from: IIT CS-331 Data Stuctures & Algorithems Lecture

class LinkedList: 
    class Node: 
        def __init__(self, val, prior=None, next=None): 
            self.val = val 
            self.prior = prior 
            self.next = next 

    def __init__(self):
        self.count = 0 
        #Sets up the sentinel node 
        self.head = LinkedList.Node(None)
        self.head.next = self.head 
        self.head.prior = self.head

    #O(1)
    def prepend(self, value):
        #Where does the element get inserted? ->after the head sentinel
        p = self.head 
        n = LinkedList.Node(value, prior=p, next=p.next)
        p.next.prior = n 
        p.next = n 

        self.count += 1 

    #O(1)
    def append(self, value): 
        #When you append: the elment geta added to the prior of the head.
        p = self.head.prior 
        n = LinkedList.Node(value, prior=p, next=p.next)
        p.next.prior = n 
        p.next = n 

        self.count += 1 

        self.count += 1 

    #O(N)
    def __getitem__(self, idx):
        assert len(self) > idx

        n = self.head.next 
        for _ in range(idx): 
            n = n.next

        return n.val

    def __len__(self):
        return self.count 

    def __iter__(self): 
        n = self.head.next 
        while n is not self.head: 
            yield n.val 
            n = n.next 

    def __repr__(self): 
        return "["+"->".join(str(x) for x in self) + "]"



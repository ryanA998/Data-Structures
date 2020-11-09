#CS 331:    IIT. Data Structures & Algorithems 
#Topic:     Lecture on Stacks. 
#Author:    Ryan Arendt 
#Source:    https://www.youtube.com/watch?v=721npTDUT9w&list=PLdrRMzNWVMEzl4G5zOlyF5BAQZ0IOFGwS&index=1

#Goal for the Stacks & Queue Implementations in class: 
#All of the operations should be done in constant time and constructed in "pythonic ways"

class Stack: 
    """ Implentation of a Stack using a Python List"""
    def __init__(self): 
        self.data = [] 

    def push(self, val):
        self.data.append(val)

    def pop(self): 
        assert not self.empty()
        return self.data.pop()

    def peek(self):
        assert not self.empty() 
        return self.data[-1]

    def empty(self): 
        return len(self.data) == 0

    def __bool__(self): 
        return not self.empty()


class LinkedStack: 
    """Linked List implementaion of a Stack."""
    class Node: 
        def __init__(self, val, next=None): 
            self.val = val 
            self.next = next 

    def __init__(self): 
        self.top = None 

    #Remeber: the links are going backwards so this makes sence 
    def push(self, val):
        self.top = LinkedStack.Node(val, self.top)

    def pop(self): 
        assert not self.empty() 
        ret = self.top.val 
        self.top = self.top.next
        return ret

    def peek(self): 
        assert not self.empty()
        return self.top.val

    def empty(self):
        return self.top is None

    def __bool__(self): 
        return not self.empty()

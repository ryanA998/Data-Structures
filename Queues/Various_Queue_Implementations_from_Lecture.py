#Lecture on Queues 
#Adapted From: IIT CS-331
#https://www.youtube.com/watch?v=dFZGYNU_YyA&list=PLdrRMzNWVMEzl4G5zOlyF5BAQZ0IOFGwS&index=2&t=73s

#Queues are linear data strucutres where we are only able add itmes 
#'enqueue' from the front and pop items 'dequeue' from the rear. Best way
#to think about queues is they are like a line at a grocery store 

#Linked List Implementation 
class Queue: 
    class Node:
        def __init__(self, val, next=None):
            self.val = val 
            self.next = next 

    def __init__(self):
        self.head = self.tail = None 

    def enqueue(self, val):
        
        if not self.tail: 
            self.head = self.tail = Queue.Node(val)
        else:
            self.tail.next = self.tail = Queue.Node(val)

    def dequeue(self):
        assert not self.empty()
        ret = self.head.val 
        self.head = self.head.next 
        #Fell off the list 
        if self.head is None: 
            self.tail = None

        return ret

    def empty(self):
        return self.head is None 

    def __boo__(self):
        return not self.empty()



#Circular Array-Backed Implementation (Not complete)
#This is constant time all around: but its of fixed size. 
#we can always resize the queue (non contant time) but we may not
#have re-size it that often.
# class Queue: 
#     def __init__(self, size): 
#         self.data = [None]*size
#         self.head = self.tail = -1 

    
#     def enqueue(self, val):
#         if self.head == -1: 
#             self.head = self.tail = 0
#             self.data[self.tail] = val

#         else: 
#             self.tail = (self.tail + 1)%len(self.data)
#             self.data[self.tail] = val

#     def dequeue(self):
#         #Assume for now there is something in th elist 
#         ret = self.data[self.head]
#         self.data[self.head] = None
#         self.head = (self.head + 1)%len(self.data)



# Linear List Implementation 
# Although this implementation gives constant time operations, it has terrible
# memory useage, since you keep adding things to the queue. Can maybe change
# with a fix length queue.
# class Queue: 
#     def __init__(self): 
#         self.data = [] 
#         self.head = self.tail = - 1

#     def enqueue(self, val):
#         if self.head == - 1: 
#             self.head = self.tail = 0
#             self.data.append(val)

#         else:
#             self.data.append(val)
#             self.tail += 1

#     def dequeue(self):
#         assert not self.empty()
#         ret = self.data[self.head]
#         #The queue is now empty
#         if self.head == self.tail:
#             self.head = self.tail = -1
#             self.data = []
#         else:
#             self.head += 1
        
#         return ret

#     def empty(self):
#         return self.tail == -1

#     def __bool__(self):
#         return not self.empty()


# q = Queue() 

# for x in range(10):
#     q.enqueue(x)

# while q:
#     print(q.dequeue())
#Simulating a Lab Printer Using a Queue in Python
#Author: Ryan Arendt
#Adapted from: https://runestone.academy/runestone/books/published/pythonds3/BasicDS/SimulationPrintingTasks.html

""" This program uses a queue to simulate the use of a printer in a computer lab. The key consideration
    in this program is minimizing the students wait time. The only thing that can be changed is the
    page rate (pages per minute: ppm). If the printer is set to a higher quality it will print pages
    slower than lower qualities. (Hight: ~5ppm. Low: 10ppm)

    Goal: To find the highest print qualility while minimizing wait time.
    
    Assumption: On average there are 10 students in the lab and on average they print twice per hour. 
    20 task/hr*(1hr/60min)*(1min/60secs) = 1task/180secs. 

    So we can assume the printer recives 1 task every 180 seconds. (3 minutes)
"""

import random

class Queue: 
    """ List implementation of a Queue. Here enqueue is an O(n) opperation and dequeue is O(1)
        Front of the Queue: end of the list. (pop last to dequeue)
        Back of the Queue: start of the list. (insert at the 0th index)
    """ 
    def __init__(self):
        self._items = [] 

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item): 
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

class Printer: 
    """ Reprents a lab printer. The printer has a fixed rate that it can 
        print pages, it has a printing task assigned to it (otherwise: None)
        and it has the time remaining to complete that task. (otherwise: 0)
    """
    def __init__(self, page_rate): 
        self.page_rate = page_rate #[pages per minute: ppm]
        self.current_task = None 
        self.time_remaining = 0

    def tick(self): 
        #Decrements the print counter if there is a current task.
        if self.current_task is not None: 
            self.time_remaining -= 1
            
            if self.time_remaining <= 0:
                self.current_task = None

    def is_busy(self): 
        return self.current_task is not None 

    def start_next(self, new_task): 
        #Coverts from pages per minute to pages per second
        page_rate_conv = 60
        self.current_task = new_task 
        self.time_remaining = new_task.get_num_pages()*page_rate_conv/self.page_rate


class Task: 
    """ Represents a single printing "Task". A Task consists of a timestamp
        that says when it was created and a number that represents the number of
        pages to be printed. minimum pages: 1 maximum pages: 20
    """
    def __init__(self, time):
        self.min_pages = 1
        self.max_pages = 20+1
        self.time_stamp = time 
        self.num_pages = random.randrange(self.min_pages, self.max_pages)

    def get_time_stamp(self):
        return self.time_stamp

    def get_num_pages(self): 
        return self.num_pages

    def wait_time(self, current_time): 
        return current_time - self.time_stamp

    
def create_new_task(job_queue, cur_time): 
    """ Simulates the creation of a random print task by the user.
        A task should be randomly created so that we on average recive a 
        new task once every 180 seconds.
    """
    rand_task = (random.randrange(1, 181) == 180) 

    if rand_task: 
        new_task = Task(cur_time)
        job_queue.enqueue(new_task)
    

def print_simulation(num_seconds, pages_per_minute): 
    """ Simulates the use of the lab printer over a specific time period (num_seconds). The simulation consists of
        the lab printer: which handles the execution of print jobs, the print queue: which handles the sceduling of 
        print jobs and a list of the current wait times for the current print simulation.
    """
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    wait_times = []

    for cur_seccond in range(num_seconds): 
        create_new_task(print_queue, cur_seccond)

        if (not lab_printer.is_busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            wait_times.append(next_task.wait_time(cur_seccond))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(wait_times)/len(wait_times)

    print(f"Avereage Wait {average_wait: 6.2f} secs" \
        +f"{print_queue.size():3d} task remaining.")


def run_simulation(time_range, page_rate, num_simulations):
    
    for i in range(num_simulations): 
        print_simulation(time_range, page_rate)


#run_simulation(3600, 10, 4)
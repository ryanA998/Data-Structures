#Implementation of a Hash Data Structure in Python.
#Adapted from: 
#https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html
#In conjunction with the CS-331 YouTube lecture series 

#In the covid_problem: Can you hash the given data based on the 
#date. (or state)

#Note: this implementation of the hash function can only deal with 
#integer key values: we can change this later if we have to. 
class HashTable: 

    def __init__(self): 
        self.size = 11
        self.slots = [None]*self.size 
        self.data = [None]*self.size 

    def put(self, key, data):
        """ Adds the key, value pair to the hash table. 
        """
        hash_value = self.hash_function(key, len(self.slots))

        #The current slot is empty: just add the data to the slot
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key 
            self.data[hash_value] = data
        
        #The current slot contains a value: decide to replace or place value in new slot
        else: 
            #The current slot has the same hash_value: replace the value in that slot
            if self.slots[hash_value] == key: 
                self.data[hash_value] = data
            # We have a collision: find the correct slot for the new value
            else: 
                next_slot = self.rehash(hash_value, len(self.slots))

                #If the next slot is empty and doesnt contain the same key
                #compute the hash value for the next slot. This loop will terminate
                #when you either reach and empty slot or reach a slot with the same key
                while self.slots[next_slot] != None and self.slots[next_slot] != key: 
                    next_slot = self.rehash(next_slot, len(self.slots))
                
                #The next slot is empty: insert the data there
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key 
                    self.slots[next_slot] = data

                #Replace the data in the next slot 
                else: 
                    self.data[next_slot] = data

    def get(self, key): 
        """ Searches the hash table for the specific key. 
        """
        start_slot = self.hash_function(key, len(self.slots))

        data = None 
        stop = False 
        found = False 

        cur_pos = start_slot 

        #While the current slot is not empty, not found and the loops not stopped
        while self.slots[cur_pos] != None and not found and not stop:
            
            #If the current slot is the key: we found it
            if self.slots[cur_pos] == key: 
                found = True 
                data = self.data[cur_pos]
            
            #Need to rehash and keep searching
            else: 
                cur_pos = self.rehash(cur_pos, len(self.slots))
                if cur_pos == start_slot:
                    stop = True
        return data
         
    #Why do we need the size as an agrument: dont we have this in the init method
    def hash_function(self, key, size):
        return key%size

    def rehash(self, old_hash, size): 
        return (old_hash+1)%size

    def __getitem__(self, key): 
        return self.get(key)

    def __setitem__(self, key, data): 
        self.put(key, data)

# ht = HashTable()

# ht[5] = "Arron Rodgers"

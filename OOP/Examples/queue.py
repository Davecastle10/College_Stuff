class Queue:
    items = []
    front = 0# in python we dont really need front and rear pointers becaus ewe could use list index's 0 and -1 to get them
    rear = -1
    length = 0# becasue we are using lists you dont really need a length


    def __init__(self, given_length):
        self.length = given_length
        
    def enqueue(self, new_item):
        self.items.append(new_item)


    def dequeue(self):
        temp = self.items[self.front]
        self.items.pop[self.front]
        return temp

    def peek():
        return self.items[self.front]


my_queue = queue(10)



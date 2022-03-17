#queue implemmentation in python
class Queue:
    def __init__(self) -> None:
        self.queue=[]
    
    #add a element
    def enqueue(self,item):
        self.queue.append(item)
    
    #remove an element
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    
    #display a queue
    
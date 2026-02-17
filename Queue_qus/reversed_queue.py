# Reverse a Queue
class Queue:
    def __init__(self):
        self.queue=[]
    
    #enqueue....insert
    def enqueue(self,q):
        self.queue.append(q)
    
    #dequeue........removed
    def dequeue(self):
        if self.is_empty():
            return -1
        return self.queue.pop(0)
    
    #revered_queue 
    def revered_queue(self):
        #first convert in stack...
        rev_que=[]
        while not self.is_empty():
            rev_que.append(self.dequeue())
        #second convert in Queue...
        while rev_que:
            self.enqueue(rev_que.pop())
        return self.queue

    #is_empty...
    def is_empty(self):
        return len(self.queue)==0
    
    #size
    def size(self):
        return len(self.queue)
    

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(f"afer reversed:{q.revered_queue()}")
print(f"queue is empty: {q.is_empty()}")
print(f"Size of Queue: {q.size()}")

class Stack:
    def __init__(self):
        self.item=[]

    #check is_empty..
    def is_empty(self):
        return len(self.item)==0
    
    #push...without append 
    def append(self,item):
        self.item +=[item]
    
    #pop....without POP
    def pop(self):
        if self.is_empty():
            return -1
        else:
            new_list=self.item[:-1]
            self.item=self.item[:-1]
            return new_list
    
    #top ...
    def check_top(self):
        return self.item[-1]
    
    #display:
    def display(self):
        return self.item
    

out_put=Stack()
out_put.append(10)
out_put.append(20)
out_put.append(30)
print(f"pop item:- {out_put.pop()}")
print(out_put.display())
print(f"CHECK List is empty:- {out_put.is_empty()}")
print(f"Top item of List:- {out_put.check_top()}")
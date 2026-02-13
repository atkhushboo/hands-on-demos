class Stack:
    def __init__(self):
        self.item=[]
    
    #push
    def push(self,items):
        return self.item.append(items)
    
    #is_empty
    def is_empty(self):
        return len(self.item)==0
    
    #pop
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        return None
    
    #reverse_stack
    def rev_st(self,input):
        for item in input:
            self.push(item)

        rev_stack=[]
        while not self.is_empty():
            rev_stack.append(self.pop())
        
        return rev_stack
    
st=Stack()
print(st.is_empty())
print(st.rev_st([1,2,3,4]))

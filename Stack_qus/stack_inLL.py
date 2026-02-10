class Stack_Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class Stack_head:
    def __init__(self):
        self.head=None
        self.lne=0
    
    #insert==append......#
    def append_val(self,val):
        new_node=Stack_Node(val)
        new_node.next=self.head
        self.head=new_node
        self.lne+=1
    
    #pop ==remove.....
    def pop_item(self):
        if self.head is None:
            return -1
        else:
            remv=self.head.data
            self.head=self.head.next
            self.lne -=1
            return remv

    # Get Top item......#
    def getTop(self):
        if self.head is None:
            return -1
        else:
            return self.head.data

    #size....of STACK...
    def stack_len(self):
        return self.lne

Stack=Stack_head()
Stack.append_val(10)
Stack.append_val(20)
Stack.append_val(30)
Stack.append_val(40)
print(Stack.pop_item())
print(Stack.getTop())
print(Stack.stack_len())
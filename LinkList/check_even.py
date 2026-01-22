# Write a function to insert a node at the beginning only if the given value is even.
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class Head_of_singly:
    def __init__(self,head=None):
        self.head=head
    
    def insert_value(self,value):
        new_node=Node(value)
        if value%2==0:
            new_node.next=self.head
            self.head=new_node
            
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
            
op=Head_of_singly()
op.insert_value(2)
op.insert_value(7)
op.insert_value(6)                
op.insert_value(4)
op.display()
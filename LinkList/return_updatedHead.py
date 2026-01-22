# Given the head of a singly linked list, write a function to insert a new node at the beginning and return the updated head.
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Singlly:
    def __init__(self,head=None):
        self.head=head
    
    def update_head(self,value):
        new_node=Node(value)
        
        new_node.next=self.head
        self.head=new_node
        return self.head

op=Singlly()
print(op.update_head("1st 12"))
print(op.update_head("2nd 102"))
print(op.update_head("4rd 1428"))

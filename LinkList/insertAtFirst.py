#insert At First ......

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Singly:
    def __init__(self,head=None):
        self.head=head
    
    def insertAtFirst(self,value):
        new_node=Node(value)

        new_node.next=self.head
        self.head=new_node
    
    def printLl(self):
        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next
        print("Empty Node")

op=Singly()
op.insertAtFirst("First Insert:-10")
op.insertAtFirst("second insert:- 20")
op.insertAtFirst("last insert:-30")
op.printLl()
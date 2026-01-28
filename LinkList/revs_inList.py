class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Header_LL:
    def __init__(self,head=None):
        self.head=head
    
    def insert_value(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    

    #....REVERSE LOGIC FOR LINKED-LIST
    def reverse_Ll(self):
        current=self.head          
        pre=None

        while current is not None:
            next_node=current.next
            current.next=pre
            pre=current
            current=next_node

        self.head=pre

    def display(self):
        temp =self.head

        while temp is not None:
            print(temp.data,end="-> ")   
            temp=temp.next
        
        print("None")

op=Header_LL()
op.insert_value(1)
op.insert_value(2)
op.insert_value(3)
op.reverse_Ll()
op.display()
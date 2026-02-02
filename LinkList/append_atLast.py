class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class Head_of_Sll:
    def __init__(self,head=None):
        self.head=head

    def append_at_last(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
        
    def display_Ll(self):
        if self.head ==None:
            print("SLL is empty.")
        else:
            curr=self.head
            while curr is not None:
                print(curr.data,end="-> ")
                curr=curr.next
            print("None")

Sll = Head_of_Sll()
Sll.append_at_last(10)
Sll.append_at_last(20)
Sll.append_at_last(30)
Sll.display_Ll()
            
#delete the value from any position:

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class Head_of_SinglyLL:
    def __init__(self,head=None):
        self.head=head
    
    def insert_at_first(self,value):
        new_node=Node(value)

        new_node.next=self.head
        self.head=new_node
    
    def del_val(self,pos):
        curr=self.head
        count=0
        while curr is not None and curr.next is not None and count<pos-1:
            curr=curr.next
            count+=1
        
        if curr is None or curr.next is None:
            print("out of range.")
            return
        curr.next=curr.next.next
    
    def display_list(self):
        temp=self.head
        if temp is None:
            print("Empty List.")
        else:
            while temp is not None:
                print(temp.data,end="--> ")
                temp=temp.next
            print("None")

out_put=Head_of_SinglyLL()
out_put.insert_at_first(10)
out_put.insert_at_first(20)
out_put.insert_at_first(30)
out_put.insert_at_first(40)
out_put.del_val(5)
out_put.display_list()
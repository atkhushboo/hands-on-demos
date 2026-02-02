class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Header_LL:
    def __init__(self,head=None):
        self.head=head
    
    def insert_at_pos(self,value,pos):
        new_node=Node(value)

        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        count=0
        while temp and count<pos-1:
            temp=temp.next
            count +=1
        
        if temp is None:
            print("Out of range.")
            return
        
        new_node.next=temp.next
        temp.next=new_node

    def display_Ll(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="-> ")
            temp=temp.next
        print("None")
    
out_put=Header_LL()
out_put.insert_at_pos(1,0)
out_put.insert_at_pos(2,1)
out_put.insert_at_pos(3,2)
out_put.display_Ll()


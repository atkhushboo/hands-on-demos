# Write a function that takes an array of integers and creates a singly linked list by inserting each element at the beginning.

class Node :
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class Head_of_SinglyLL:
    def __init__(self,head=None):
        self.head=head
    
    def insert_in_start(self,value):
        new_list=Node(value)
        
        new_list.next=self.head
        self.head=new_list
    
    def element_in_list(self,arr):
        for item in arr:
        
            self.insert_in_start(item)
            
    def display_list(self):
        temp=self.head
        arr=[]
        while temp is not None:
            arr.append(temp.data)
            temp=temp.next
        return arr
        
out_put=Head_of_SinglyLL()
out_put.element_in_list([1,2,3,4])
print(out_put.display_list())
    
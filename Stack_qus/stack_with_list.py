class Stack:
    def __init__(self):
        self.item=[]

    def is_empty(self):
        return len(self.item)==0
    def push(self,item):
        return self.item.append(item)
    def pop(self):
        if len(self.item)==0:
            return "We don't have item to remove."
        else:
            removed_item=self.item.pop()
            return removed_item
    def top(self):
        return self.item[-1]
    def sizee(self):
        return (len(self.item))

ot=Stack()
ot.push(5)
ot.push(6)
ot.push(8)
print(f"Stack contant -> {ot}")
print(f"Check Stack is empty -> {ot.is_empty()}")
print(f"Pop item from stack -> {ot.pop()}")  
print(f"Top element of Stack after Pop => {ot.top()}")
print(f"Size of Stack => {ot.sizee()}")              


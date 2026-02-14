class Stack_balance:
    def __init__(self):
        self.item=[]
    
    #is_empty...
    def is_empty(self):
        return len(self.item)==0
    #Push.....append
    def push(self,item):
        return self.item.append(item)

    #Pop.....
    def pop(self):
        if self.is_empty():
            return
        return self.item.pop()
    
    #check_brackets...
    def check_bracket(self,value):
        for char in value:
            if char in "({[":
                self.item.append(char)
            elif char in "]})":
                if self.is_empty():     #if stack is empty then return 
                    return False

                top=self.pop()  #otherwise pop and store in top 
                if char ==")" and top !="(":
                    return False
                if char=="}" and top !="{":
                    return False
                if char =="]" and top !="[":
                    return False
            
        return self.is_empty()
    #stack print....
    def display(self):
        return self.item

st=Stack_balance()
print(st.check_bracket("()"))
print(st.check_bracket("{}"))
print(st.check_bracket("["))
print(st.check_bracket(")"))
print(f"\nStack: {st.display()}")



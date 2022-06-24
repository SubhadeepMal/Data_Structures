#Stacks:

class node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class stack:
    def __init__(self, value):
        new_node = node(value)
        self.top=new_node
        self.height=1
    
    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def push(self, value):
        new_node=node(value)
        new_node.next=self.top
        self.top=new_node
        self.height+=1

    def pop(self):
        if self.height==0:
            return "Empty!"
        temp=self.top
        self.top=temp.next
        temp=None
        self.height-=1


s1=stack(1)
# s1.print_stack()

for i in range(2,6):
    s1.push(i)
s1.print_stack()

print("Pop: ")
s1.pop()
s1.pop()
s1.print_stack()

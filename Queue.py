#Queue:

from imp import new_module


class node:
    def __init__(self, value):
        self.value= value
        self.next= None

class queue:
    def __init__(self, value):
        new_node= node(value)
        self.first= new_node
        self.last= new_node
        self.length=1

    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def enqueue(self, value):
        new_node= node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1

    def dequeue(self):
        if self.length==0:
            return "Empty!"
        temp=self.first
        if self.length==1:
            self.first=self.last= None
        else:
            self.first=temp.next
            temp=None
        self.length-=1

q1=queue(10)
q1.print_queue()

print("Enqueue: ")
for x in range(20,70,10):
    q1.enqueue(x)
q1.print_queue()

print("Pop: ")
q1.dequeue()
q1.print_queue()



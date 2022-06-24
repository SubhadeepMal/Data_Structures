#LINKED_LIST:

class node:
    def __init__(self, value):
        self.value= value
        self.next= None

class Linklist:
    
    def __init__(self, value):
        new_node=node(value)
        self.head= new_node
        self.tail= new_node
        self.length= 1

    def print_list(self):
        k=self.head
        while k is not None:
            print(k.value)
            k= k.next

    def append_list(self,value):
        new_node=node(value)
        if self.length==0:
            self.head=new_node
            self.tail= new_node
        else:
            self.tail.next= new_node
            self.tail= new_node
        self.length= self.length+1

    def pop_list(self):
        if self.length==0:
            return "Empty List"
        else:
            temp=self.head
            pre=temp
            while temp.next is not None:
                pre= temp
                temp=temp.next
            self.tail= pre
            self.tail.next= None      #popping the last element
            self.length-=1
            if self.length ==0:
                self.head=None
                self.tail=None
            return temp.value

    def prepend(self, value):
        new_node= node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next= self.head
            self.head= new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length==0:
            return "EMPTY"
        temp=self.head
        self.head= self.head.next
        temp.next= None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value

    def get(self, index):
        if index<0 or index>=self.length:
            return "INVALID Index"
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def set(self, index, value):
        if index<0 or index>=self.length:
            return "INVALID Index"
        temp=self.head
        a=0
        while a!=index:
            temp=temp.next
            a+=1
        else:
            temp.value=value
        return temp.value

    def insert(self, index, value):
        if index<0 or index>self.length:
            return "Invalid"
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append_list(value)        
        new_node= node(value)
        temp= self.get(index-1)
        new_node.next= temp.next
        temp.next= new_node
        self.length+=1
        return True
        
    def remove(self, index):
        if index<0 or index>=self.length:
            return "Invalid"
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop_list()
        
        prev= self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next= None
        self.length-=1
        return temp

    def reverse(self):
        temp=self.head
        self.head= self.tail
        self.tail=temp

        after= temp.next
        before= None
        for _ in range(self.length):
            after= temp.next
            temp.next= before
            before= temp
            temp=after
        

l1=Linklist(0)
#print(l1.head.value)
print("Append: ")
l=[1,2,3,4]
for x in l:
    l1.append_list(x)

print("Linked List values: ")
l1.print_list()
'''
print("Head value: ",l1.head.value)
print("Tail value: ",l1.tail.value)
print("Length of linkedList: ",l1.length)

print("pop: ")
print(l1.pop_list())
print("Length of New linkedList: ",l1.length)

print("Linked List values After Pop: ")
l1.print_list()
#print(l1.pop_list())
#print(l1.pop_list())
#print(l1.pop_list())

print("New linked list after Prepend: ")
l1.prepend(-1)
l1.print_list()

print(l1.pop_first())

print("Value at index:1= ",l1.get(1))
print(l1.set(1,5))
l1.print_list()

l1.insert(3,9)

print(l1.remove(1))'''

l1.reverse()

l1.print_list()


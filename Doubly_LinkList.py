## Doubly LinkList

class node:
    def __init__(self, value):
        self.value= value
        self.next= None
        self.prev= None

class DLL:
    def __init__(self,value):
        new_node=node(value)
        self.head=new_node
        self.tail=new_node
        self.length =1

    def print_list(self):
        temp= self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def append_list(self, value):
        new_node= node(value)
        if self.length==0:
            self.head= self.tail=new_node
        else:
            temp=self.tail
            self.tail.next= new_node
            self.tail= new_node
            self.tail.prev= temp
        self.length+=1

    def pop_list(self):
        if self.length==0:
            return "Empty List!"
        if self.length==1:
            self.head=self.tail=None
        else:
            temp=self.tail.prev
            temp.next= None
            self.tail=temp
        self.length-=1
    
    def prepend(self,value):
        new_node=node(value)
        if self.length==0:
            self.head= self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            self.head.prev=None
        self.length+=1
        
    def pop_first(self):
        if self.length==0:
            return "Empty List!"
        temp=self.head
        temp2=self.head.next
        temp2.prev=None
        self.head=temp2
        temp=None
        self.length-=1

    def get(self,index):
        if index<0 or index>=self.length:
            return "INVALID Index"
        temp=self.head
        for x in range(index):
            temp=temp.next
        return temp.value

    def insert_list(self,index,value):
        new_node=node(value)
        if index<0 or index>self.length:
            return "INVALID Index"
        
        else:
            temp=self.head
            pre=None
            for x in range(index):
                pre=temp
                temp=temp.next
            pre.next=new_node
            new_node.prev=pre
            new_node.next=temp
            temp.prev=new_node
            self.length+=1

    def set(self,index,value):
        if index<0 or index>=self.length:
            return "INVALID Index"
        temp=self.head
        for x in range(index):
            temp=temp.next
        temp.value=value
    
    def remove(self,index):
        if index<0 or index>=self.length:
            return "INVALID"
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop_list()
        temp= self.head
        pre=temp
        for x in range(index):
            pre=temp
            temp=temp.next
        pre.next=temp.next
        temp.next.prev=pre
        temp=None
        return 


new=DLL(5)
#print(new.head.value)
#new.print_list()

# print("Appending: ")
# for x in range(6,10):
#     new.append_list(x)
# new.print_list()

# print("After pop: ")
# new.pop_list()
# new.print_list()
# print(new.pop_list())

# print("Prepend: ")
# new.prepend(4)
# new.prepend(3)
# new.print_list()

# print("Pop_first: ")
# new.pop_first()
# new.print_list()

# print("Get: ")
# print(new.get(0))

# print("Insertion: ")
# new.insert_list(2,11)
# new.print_list()

# print("Set: ")
# print(new.set(5,0))
# new.print_list()

# print("Removed : ")
# new.remove(3)
# new.print_list()
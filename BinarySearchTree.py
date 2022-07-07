#BinarySearchTree (BST):

from unittest.mock import NonCallableMagicMock


class Node:
    def __init__(self, value):
        self.value= value
        self.left= None 
        self.right= None

class BST:
    def __init__(self):
        self.root=None

    def insert(self, value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

    def contains(self, value):
        temp= self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node= current_node.left
        return current_node

    # Bredth First Search (BFS):
    def BFS(self):
        current_node= self.root
        queue=[]
        results=[]
        queue.append(current_node)

        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
            
    # DFS Pre_order:
    def DFS_preorder(self):
        results=[]
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results        

mytree= BST()
#print(mytree.root)

#print("Insert: ")
mytree.insert(5)
mytree.insert(2)
mytree.insert(7)
mytree.insert(4)
mytree.insert(9)
mytree.insert(1)
mytree.insert(6)
# print(mytree.root.value)
# print(mytree.root.left.value)
# print(mytree.root.right.value)

# print("Contains: ")
# print(mytree.contains(7))
# print(mytree.contains(3))

# print("Minimum value: ")
# print(mytree.min_value_node(mytree.root).value)
# print(mytree.min_value_node(mytree.root.right).value)

#print("Breadth First Search: ")
# print(mytree.BFS())

print("Depth First Search-> Pre_Order: ")
print(mytree.DFS_preorder())
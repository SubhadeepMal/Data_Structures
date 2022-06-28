#Hashtable:

class HashTable:

    def __init__(self, size=7):
        self.data_map=[None]*size

    def __hash(self, key):
        my_hash= 0
        for letter in key:
            my_hash= (my_hash+ ord(letter)* 11)% len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index= self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index= self.__hash(key)
        if self.data_map[index] is not None:
            for x in range(len(self.data_map[index])):
                if self.data_map[index][x][0]== key:
                    return self.data_map[index][x][1]
        return None

    def keys(self):
        allkey=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    allkey.append(self.data_map[i][j][0])
        return allkey


my_hashtable=HashTable()

my_hashtable.set_item('bolts', 40)
my_hashtable.set_item('washers', 50)
my_hashtable.set_item('lumber', 70)

# my_hashtable.print_table()  

# print(my_hashtable.get_item('bolts'))
# print(my_hashtable.get_item('washers'))
# print(my_hashtable.get_item('lumber'))

print(my_hashtable.keys())

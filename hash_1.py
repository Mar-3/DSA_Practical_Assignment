## BM40A1500 Data Structures and Algorithms  -  Practical assignment
## Marko Jutila - hash_1.py
## 01.12.2022

## Node class is used for chaining together values in same array using linked lists
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
## Hash class is used to store the hash table and methods for accessing it
class Hash:
    
    # Constructior method, initializes a hash table the size of hash size-variable and fills it with empty node-objects
    def __init__(self, size):
        self.hashTable = []
        self.size = size
        for i in range(0, size):
            self.hashTable.append(Node(None,None))

    # The original fold() method, replaced by more efficient djb2 folding algorithm
    # def fold(self, value):
    #     # fold the value to get index:
    #     foldedSum = 0
    #     mul = 1
    #     value = str(value)
    #     # Folding algorithm is the one used in OpenDSA: Hashing -materials
    #     for i in range(0, len(value)):
    #         if (i % 4 == 0):
    #             mul = 1
    #         else:
    #             mul = mul*256
    #         foldedSum+=ord(value[i]) * mul

    #     index = foldedSum%self.size
    #     return index
    

    # djb2, used this site as reference: https://theartincode.stanis.me/008-djb2/
    def fold(self, value):
        sum = 5381
        value = str(value)
        # every loop: sum = (sum * 3) + ASCII vlaue of character
        # Uses bitshift operators for efficiency
        for i in range(0, len(value)):
            sum = ((sum << 5) + sum) + ord(value[i])

        index = sum%self.size # index using modulo(size of table)
        return index

    # Insert function inserts the new value to the hash table
    def insert(self, value):
        # Goes through the linked list and adds the value to the end of the list if not found.
        index = self.fold(value)
        node = self.hashTable[index]
        if (node.value == None):
            node.value = value
            return None
        while (node.next != None):
            if (node.value == value):
                return None
            node = node.next
        node.next = Node(value, None)
        return None

    # Deletes a value from the hash table
    def delete(self, value):
        index = self.fold(value)
        node = self.hashTable[index]
        previousNode = None
        # Goes through the linked list and using object references
        # deletes the wanted value from the table
        while (node != None):
            if node.value == value:
                if (previousNode == None):
                    self.hashTable[index].value = None
                else:
                    previousNode.next = node.next
                break
            previousNode = node
            node = node.next
        return None

    # Searches for a value from the hash table, returns true if value found, false if not.
    def search(self, value):
        index = self.fold(value)
        node = self.hashTable[index]
        while (node != None):
            if node.value == value:
                return True
            node = node.next
        return False

    # Prints all the contents of the hash, differentiates which values are on the
    # same index slot in a linked list.
    def print(self):
        for slot in self.hashTable:
            if slot.value == None:
                print("[]")
            else:
                node = slot
                while (node != None):
                    print(node.value, end='->') 
                    node = node.next
                print("[]")
        return None

if __name__ == "__main__":
    hash = Hash(3)

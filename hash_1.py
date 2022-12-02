## BM40A1500 Data Structures and Algorithms  -  Practical assignment
## Marko Jutila - hash_1.py
## 01.12.2022

class Node:
    ## Node class is used for chaining together values in same array using linked lists
    def __init__(self, value, next):
        self.value = value
        self.next = next
    

class Hash:
    def __init__(self, size):
        self.size = size
        self.slots = [Node(None, None)]*size

    def fold(self, value):
        # fold the value to get address:
        foldedSum = 0
        mul = 1
        value = str(value)
        # Folding algorithm is the one used in OpenDSA: Hashing -materials
        for i in range(0, len(value)):
            if (i % 4 == 0):
                mul = 1
            else:
                mul = mul*256
            foldedSum+=ord(value[i]) * mul

        address = foldedSum%self.size
        return address
            

    def insert(self, value):
        address = self.fold(value)
        node = self.slots[address]
        while (node != None):
            if node.value == value:
                return None
            node = node.next
        node = Node(value, None)
        return None


    def delete(self, value):
        address = self.fold(value)
        # If nothing found on the address, returns None
        node = self.slots[address]
        previousNode = None
        while (node != None):
            if node.value == value:
                if (previousNode == None):
                    self.slots[address] = node.next
                else:
                    previousNode.next = node.next
                break
            previousNode = node
            node = node.next
        return None

    def search(self, value):
        # Search method returns true if value found, false if not.
        address = self.fold(value)
        node = self.slots[address]
        while (node != None):
            if node.value == value:
                return True
            node = node.next
        return False

    def print(self):
        # Prints all the contents of the hash, differentiates which values are on the
        # same address slot in a linked list.
        for slot in self.slots:
            if slot.value != None:
                node = slot
                print("These are same address:")
                while (node != None):
                    print(node.value)
                    node = node.next
                print("END")
        return None




if __name__ == "__main__":
    hash = Hash(3)
    hash.insert(123213)
    hash.insert('hashtable')
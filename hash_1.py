## BM40A1500 Data Structures and Algorithms  -  Practical assignment
## Marko Jutila - hash_1.py
## 01.12.2022



#

class Node:
    ## Node class is used for chaining together values in same array using linked lists
    def __init__(self, value, next):
        self.value = value
        self.next = next
    

class Hash:
    def __init__(self, size):
        self.size = size
        self.slots = [None]*size

    # https://www.geeksforgeeks.org/folding-method-in-hashing/ used for
    # understanding the folding method in hashing.
    def fold(self, value):
        # fold the value to get address:
        folded = []
        new_string = ''
        foldedSum = 0
        value = str(value)
        ## This folding algorithm chops the string/int to 2 character long parts. Then squares them and sums up all the
        ## squared parts to get the dividant for the address. 
        for i in range(0,len(value)-1,2):
                new_string = str(int(str(ord(value[i]))+str(ord(value[i+1]))))
                folded.append(int(new_string)^2)
        foldedSum = sum(folded)
        address = foldedSum%self.size
        return address
            

    def insert(self, value):
        address = self.fold(value)
        # If slot is empty, fill it with a new node
        if self.slots[address] == None:
            self.slots[address] = Node(value, None)
        else:
        # If occupied, add a new node to the end of the linked list.
            node = self.slots[address]
            while (node.next != None):
                node = node.next
            node.next = Node(value, None)
        return None


    def delete(self, value):
        address = self.fold(value)

        if self.slots[address] == None:
            return None
        elif self.slots[address].value == value and self.slots[address].next == None:
            self.slots[address] = None
            return None
        else:
            node = self.slots[address]
            previousNode = None
            # While loop for going through the linked list
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
            if slot == None:
                print("[]")
            else:
                node = slot
                print("These are same address:")
                while (node != None):
                    print(node.value)
                    node = node.next
                print("END")
        return None




if __name__ == "__main__":
    hash = Hash(3)

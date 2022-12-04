## BM40A1500 Data Structures and Algorithms  -  Practical assignment
## XXXXXX - hash_2.py
## 04.12.2022

# 2. Testing and Analyzing the Hash Table

from hash_1 import Hash
import time

if __name__ == "__main__":
    hash = Hash(3)


    # Testing running time for inserting a new value with 2 different values:
    startTimeSeconds = time.time()
    hash.insert('hashtable')
    
    insert1TimeSeconds = time.time()
    hash.insert(12)
    insert2TimeSeconds = time.time()
    
    # Other inserts
    hash.insert(1234)
    hash.insert(4328989)
    hash.insert('BM40A1500')
    hash.insert(-12456)
    hash.insert('aaaabbbbcccc')
    hash.print()
    print()

    # Testing search for a word running times with 2 different words:
    searchStartTimeSeconds = time.time()
    search1 = hash.search(-12456)
    search1TimeSeconds = time.time()
    search2 = hash.search('hashtable')
    search2TimeSeconds = time.time()

    # Printing the results
    print("-12456 found: " + str(search1))
    print("'hashtable' found: " + str(search2))
    print("1235 found: " + str(hash.search(1235)))
    print()

    # Testing delete value running time with 2 different values:
    deleteStartTimeSeconds = time.time()
    hash.delete('BM40A1500')
    delete1TimeSeconds = time.time()
    hash.delete(1234)
    delete2TimeSeconds = time.time()
    hash.delete('aaaabbbbcccc')

    hash.print()

    # Running times for operations:
    print()
    print("Running times:")
    print("Insert 12: " + str(insert1TimeSeconds-startTimeSeconds))
    print("Insert 'hashtable': " + str(insert2TimeSeconds-insert1TimeSeconds))
    print("Search -123456: " + str(search1TimeSeconds-searchStartTimeSeconds))
    print("Search 'hashtable': " + str(search2TimeSeconds-search1TimeSeconds))
    print("Delete 'BM40A1500': " + str(delete1TimeSeconds-deleteStartTimeSeconds))
    print("Delete 1234: " + str(delete2TimeSeconds-delete1TimeSeconds))
from hash_1 import Hash

if __name__ == "__main__":
    hash = Hash(3)

    hash.insert(12)
    hash.insert('hashtable')
    hash.insert(1234)
    hash.insert(4328989)
    hash.insert('BM40A1500')
    hash.insert(-12456)
    hash.insert('aaaabbbbcccc')
    hash.print()

    print("-123456 found: " + str(hash.search(-123456)))
    print("'hashtable' found: " + str(hash.search('hashtable')))
    print("1235 found: " + str(hash.search(1235)))

    hash.delete('BM40A1500')
    hash.delete(1234)
    hash.delete('aaaabbbbcccc')

    hash.print()
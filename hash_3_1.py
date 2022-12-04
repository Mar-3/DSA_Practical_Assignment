## BM40A1500 Data Structures and Algorithms  -  Practical assignment
## XXXXXX - hash_3_1.py
## 01.12.2022

# 3. The Pressure Test
# Testing hash table performance.

from hash_1 import Hash
import sys
import time

if __name__ == "__main__":
    # Initializing the Hash-table
    initializeStartTimeSeconds = time.time()
    hash = Hash(10000)
    initializeDoneTimeSeconds = time.time()
    commonWords = 0
    file1Name = "kaikkisanat.txt"
    file2Name = "words_alpha.txt"

    try:
        #Reading the file and inserting words
        insertsStartTimeSeconds = time.time()
        tiedosto = open(file1Name, 'r')
        row = tiedosto.readline()[:-1]
        while (row != ''):
            hash.insert(row)
            row = tiedosto.readline()[:-1]
        tiedosto.close()
        insertsDoneTimeSeconds = time.time()

        ## Reading the second file and searching for the cmmon words
        searchStartTimeSeconds = time.time()
        tiedosto = open(file2Name, 'r')

        row = tiedosto.readline()[:-1]
        while (row != ''):
            if hash.search(row):
                commonWords+=1
            row = tiedosto.readline()[:-1]
        tiedosto.close()
        searchDoneTimeSeconds = time.time()

        ## Final prints and times:
        #hash.print() # Fir printing the contents of hash table, quite unpractical with 10 000 words...
        print("Initializing the hash table: " + str(initializeDoneTimeSeconds-initializeStartTimeSeconds) + "s")
        print("Adding the words: " + str(insertsDoneTimeSeconds-insertsStartTimeSeconds) + "s")
        print("Finding the common words: " + str(searchDoneTimeSeconds-searchStartTimeSeconds) + "s")
        print("All: " + str((initializeDoneTimeSeconds-initializeStartTimeSeconds)+(insertsDoneTimeSeconds-insertsStartTimeSeconds)+(searchDoneTimeSeconds-searchStartTimeSeconds)))
        print("Common words: " + str(commonWords))
    except Exception as e:
        print("Error. Quitting..")
        print(e)
        sys.exit(0)

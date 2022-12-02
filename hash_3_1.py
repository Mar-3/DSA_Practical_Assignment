from hash_1 import Hash
import sys
import time

if __name__ == "__main__":
    # Initializing the ne Hash-table and taking 
    initializeStartTimeSeconds = time.time()
    hash = Hash(10000)
    initializeDoneTime = time.time()
    sum = 0
    row = None
    file1Name = "kaikkisanat.txt"
    file2Name = "words_alpha.txt"
    words1List = []
    words2List = []
    
    
    try:
        tiedosto = open(file1Name, 'r')
        row = tiedosto.readline()[:-1]
        while (row != ''):
            words1List.append(row)
            row = tiedosto.readline()[:-1]
        tiedosto.close()

        insertsStartTimeSeconds = time.time()

        for word in words1List:
            hash.insert(word)

        insertsDoneTimeSeconds = time.time()

        tiedosto = open(file2Name, 'r')
        row = tiedosto.readline()[:-1]
        while (row != ''):
            words2List.append(row)
            row = tiedosto.readline()[:-1]
        tiedosto.close()
        
        searchStartTimeSeconds = time.time()

        for word in words2List:
            if hash.search(word):
                sum+=1

        searchDoneTimeSeconds = time.time()
        hash.print()
        print("Initializing the hash table: " + str(initializeDoneTime-initializeStartTimeSeconds) + "s")
        print("Adding the words: " + str(insertsDoneTimeSeconds-insertsStartTimeSeconds) + "s")
        print("Finding the common words: " + str(searchDoneTimeSeconds-searchStartTimeSeconds) + "s")
        print(sum)
    except Exception as e:
        print("Error in file handling. Quitting")
        print(e)
        sys.exit(0)

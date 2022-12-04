import sys
import time

if __name__ == "__main__":
    # Initializing the ne Hash-table and taking 
    initializeStartTimeSeconds = time.time()
    words1List = []
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
            words1List.append(row)
            row = tiedosto.readline()[:-1]
        tiedosto.close()
        insertsDoneTimeSeconds = time.time()

        ## Reading the second file and searching for the words
        searchStartTimeSeconds = time.time()

        tiedosto = open(file2Name, 'r')
        row = tiedosto.readline()[:-1]
        while (row != ''):
            if row in words1List:
                commonWords+=1
            row = tiedosto.readline()[:-1]
        tiedosto.close()
        
        searchDoneTimeSeconds = time.time()

        ## Final prints and times:
        print("Initializing the list: " + str(initializeDoneTimeSeconds-initializeStartTimeSeconds) + "s")
        print("Adding the words to the list: " + str(insertsDoneTimeSeconds-insertsStartTimeSeconds) + "s")
        print("Finding the common words: " + str(searchDoneTimeSeconds-searchStartTimeSeconds) + "s")
        print("Common words: " + str(commonWords))
    except Exception as e:
        print("Error in file handling. Quitting")
        print(e)
        sys.exit(0)

#Count of words, lines and characters from a .txt file. 
def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open(fileName, 'r') as file:
        for line in file:
            numlines += 1
            wordlist = line.split()
            numwords += len(wordlist)
            numchars += len(line)

    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Characters: ", numchars)

countWords("Names.txt")
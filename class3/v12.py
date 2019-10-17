import sys

def safe_open(filename):
    try:
        fo = open( filename, "r" )
        return( fo )
    except:
        print( "File open failed: %s", (filename) )
        sys.exit(-1)


def safe_input(fo):
    try:
        lineOfWords = fo.readline().strip()
        if lineOfWords == "":
            return( "", False )
        else:
            return( lineOfWords, True )
    except:
        return( "", False )

def main():
    targetWords = [ ]
    uniqueWords = [ ]

    theCount = 0
    cFlag = True

    twfo = safe_open( "target.words.txt" )
    targetWords, cFlag = safe_input(twfo)
    twfo.close()
    # print( "Target words 1: ", targetWords )
    targetWords = targetWords.split()
    # print( "Target words 2: ", targetWords )

    wordsfo = safe_open( "weather.v2.txt" )

    while cFlag:
        lineOfWords, cFlag = safe_input(wordsfo)
        if not cFlag:
            break

        positive = False
        for word in lineOfWords.split():

          # First word is special 
          firstWord = False
          if lineOfWords.split().index(word) == 0:
            firstWord = True
            if word == 'true':
              print('+/', end='')
            else:
              print('-/', end='')

          else:
            if word in targetWords and not firstWord:
               theCount = theCount + 1
               positive = True
               # print( "+: ", lineOfWords )

            if word not in uniqueWords:
                uniqueWords.append(word)

        listOfWords = lineOfWords.split()
        listOfWords.pop(0)
        if positive:
            print( "+: ", ' '.join(listOfWords) )
        else:
            print( "-: ", ' '.join(listOfWords) )


        # print(theCount)
    wordsfo.close()
    print( "Target words: ", targetWords )
    print( "Unique word count: %d" % (len(uniqueWords)), uniqueWords[0:5])

if __name__ == "__main__":
    main()

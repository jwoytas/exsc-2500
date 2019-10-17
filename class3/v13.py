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

    linesOfData = 0
    tpCount = 0
    tnCount = 0
    fpCount = 0
    fnCount = 0

    while cFlag:
        lineOfWords, cFlag = safe_input(wordsfo)
        if not cFlag:
            break

        linesOfData = linesOfData + 1

        # Split the string lineOfWords into the Class and the Phrase
        theLine = lineOfWords.split()
        theClass = theLine[0]
        thePhrase = theLine[1:]

        positive = False

        for word in thePhrase:

          if word in targetWords:
            theCount = theCount + 1
            positive = True
            # print( "+: ", lineOfWords )

          if word not in uniqueWords:
            uniqueWords.append(word)

        if positive and theClass in ['true','True', 't', 'T']:
          print( "+/+:TP: ", end='')
          tpCount = tpCount + 1
        elif positive and theClass in ['false','False', 'f', 'F']:
          print( "+/-:FP: ", end='')
          fpCount = fpCount + 1
        elif not positive and theClass in ['true','True', 't', 'T']:
          print( "-/P:FN: ", end='')
          fnCount = fnCount + 1
        elif not positive and theClass in ['false','False', 'f', 'F']:
          print( "-/-:TN: ", end='')
          tnCount = tnCount + 1
        else:
          print('?: ', end='')

        print(' '.join(thePhrase))

        # print(theCount)
    wordsfo.close()
    print( "The number of lines/training instances ", linesOfData)
    print('TP:   %d  TN:  %d', (tpCount, tnCount))
    print('FP:   %d  FN:  %d', (fpCount, fnCount))

    print('Precision: ', tpCount / (tpCount+tnCount))
    print('Recall: ')

    print( "Target words: ", targetWords )
    print( "Unique word count: %d" % (len(uniqueWords)), uniqueWords[0:5])

if __name__ == "__main__":
    main()

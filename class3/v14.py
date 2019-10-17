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
    #targetWords = targetWords.split()
    # print( "Target words 2: ", targetWords )

    wordsfo = safe_open( "weather.v2.txt" )

    linesOfData = 0
    tpCount = 0
    fpCount = 0
    tnCount = 0
    fnCount = 0

    trueList = ['true','True', 't', 'T']
    falseList = ['false','False', 'f', 'F']

    possibleTW = []
    possibleTWcount = []

    while cFlag:
        lineOfWords, cFlag = safe_input(wordsfo)
        if not cFlag:
            break

        linesOfData += 1

        # Split the string lineOfWords into the Class and the Phrase
        theLine = lineOfWords.split()
        theClass = theLine[0]
        thePhrase = theLine[1:]

        positive = False

        if theClass in trueList:
          for word in thePhrase:

            if word not in possibleTW:
              possibleTW.append(word)
              possibleTWcount.append(1)
            else:
              i = possibleTW.index(word)
              possibleTWcount[i] += 1

          print(possibleTW)
          print(possibleTWcount)

          index = possibleTWcount.index(max(possibleTWcount))
          #mostOccured = max(possibleTWcount)

          index2 = 0
          if index >= 2:
            index2 = possibleTWcount.index(max(possibleTWcount)-1)

          bestWord = possibleTW[index]
          secondbestWord = possibleTW[index2]



        targetWords = [bestWord, secondbestWord]

        for word in thePhrase:

          if word in targetWords:
            theCount = theCount + 1
            positive = True
            # print( "+: ", lineOfWords )

          if word not in uniqueWords:
            uniqueWords.append(word)

        if positive and theClass in trueList:
          print( "+/+:TP: ", end='')
          tpCount += 1
        elif positive and theClass in falseList:
          print( "+/-:FP: ", end='')
          fpCount += 1
        elif not positive and theClass in trueList:
          print( "-/+:FN: ", end='')
          fnCount += 1
        elif not positive and theClass in falseList:
          print( "-/-:TN: ", end='')
          tnCount += 1
        else:
          print('?: ', end='')

        print(' '.join(thePhrase))


    wordsfo.close()
    print( "The number of lines/training instances ", linesOfData)
    print('TP:   %3d  TN:  %3d' % (tpCount, tnCount))
    print('FP:   %3d  FN:  %3d' % (fpCount, fnCount))

    precision = (1.0*tpCount) / (tpCount+fpCount)
    recall =  (1.0*tpCount) / (tpCount+fnCount)
    print('Precision: %5f Recall: %5f' % (precision, recall))

    print( "Target words: ", targetWords )
    print( "Unique word count: %d" % (len(uniqueWords)), uniqueWords[0:5])

if __name__ == "__main__":
    main()

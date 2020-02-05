# This program reads text input and counts the number of "Target" words.
# It also counts the number of occurances of each unique word

import sys
import string

# This method will attempt to open the file
#   Accepts: string filename
#   Returns: fileobject
#   Handles exceptions by quiting the program
def safe_open(filename):
  try:
    fo = open(filename, "r")
    return(fo)
  except:
    print("File open failed: %s" % (filename))
    sys.exit(-1)

# This method will attempt to read a line of input from a file
#   Accepts: fileobject fo
#   Returns: list (of words)
#   Handles exceptions returning an empty string
def safe_input(fo):
  try:
    lineOfWords = fo.readline().strip()  # Remove the newline char from readline()
    if lineOfWords == "":
      return ("")  # Blank line or EOF
    else:
      return (lineOfWords)
  except:
    return("")

# This method will normalize strings in a given list
# It will remove all punctuation, convert the word to lowercase and
# it will remove any duplicate words
#   Accepts: list listOfWords
#   Returns: list
def normalize_data(listOfWords):
  newWordList = []          # Return this 'clean' list of words
  for word in listOfWords:

    # Remove punctuation and convert to lower case
    # - credit: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = word.lower()

    # Remove any duplicate words
    if word not in newWordList:
      newWordList.append(word)

  return newWordList

# This method will read all lines from a file and return a list of lists that contain each line and words
#   Accepts: string filename
#   Returns: list of (list of strings)
def readDataWords(filename):

  wList = []          # A list of lists of all the data words
  curList = []        # Current list for each line of text

  fo = safe_open(filename)  # Open the file and catch any io errors

  while True:

    lineOfWords = safe_input(fo)   # Read from the file and catch any errors

    if lineOfWords == "":          # End of data or error exception, break
      break

    curList = lineOfWords.split()      # Split the line string and save as a list
    curList = normalize_data(curList)  # Remove punctuation, duplicates and convert to lowercase

    wList.append(curList)   # Add the current list of words to the whole file list

  fo.close()                # All data has been read, close the file
  return wList

# This method will display the targetWords, uniqueWords and the
#   number of times each unqiue word was encountered in the file
#   Accepts: list, list, list
def printDetails(targetWords, linesOfData, tpCount, tnCount, fpCount, fnCount):
  print('------------------------------------------------------------')
  print('The target words are: ', targetWords)
  print('------------------------------------------------------------')
  print( "The number of lines/training instances ", linesOfData)
  print('------------------------------------------------------------')
  print('TP:   %3d  TN:  %3d' % (tpCount, tnCount))
  print('FP:   %3d  FN:  %3d' % (fpCount, fnCount))
  print('------------------------------------------------------------')
  precision = (1.0*tpCount) / (tpCount+fpCount)
  recall =  (1.0*tpCount) / (tpCount+fnCount)
  print('Precision: %f \nRecall: %f' % (precision, recall))
  print('------------------------------------------------------------')

# Will check if the given word is in the uniqueWords list
#   If it is not, the word will be added
#   If it is, the word will be counted in the associated cound list
#   Accepts: string, list, list
def addOrIncrement(word, uniqueWords, uniqueCount):

  if word not in uniqueWords:
    # This word has not been seen before, lets remember it and count it
    uniqueWords.append(word)            # Found a unique word
    uniqueCount.append(1)           # Count starts at one
  else:
    # This word has been seen before, lets increment its count
    i = uniqueWords.index(word)         # The word is not unique
    uniqueCount[i] =  uniqueCount[i] + 1  # Increment the word counter

  return uniqueWords, uniqueCount


#####################################
### Program execution begins here ###
#####################################
def main():
  # Initialize variables
  # twFileName = 'target.words.txt'         # Target Words file
  # dataFileName = 'weather.v2.txt'         # Data Words file
  dataFileName = 'movie_review.txt'

  trueList =  ['true', 't']   # constant values
  falseList = ['false', 'f']

  linesOfData = 0       # Count lines of data for stats

  # These counters will be used to calculate Precision and Recall
  tpCount, fpCount, tnCount, fnCount = (0,0,0,0)

  # Changing target word functionality
  targetWords = []

  # Initially we will keep track unique words for 'true' and 'false' ground thruths
  trueUniqueWords = []
  trueCount = []
  falseUniqueWords = []
  falseCount = []


  # The data List will contain lists for each line of the file. Those lists will contain words
  dataList = readDataWords(dataFileName)


  ## First loop will look count unqiue words for both true and false statements
  for lineOfWords in dataList:      #  For each line (list) of words...

    # The first word of each line represents "Ground Truth"
    groundTruth = lineOfWords[0].lower()

    for word in lineOfWords[1:]:    # For each word (except the first word)...

      # Track unique words and number of occurances in two categories, (true or false)
      if groundTruth in trueList:
        trueUniqueWords, trueCount = addOrIncrement(word, trueUniqueWords, trueCount)
      elif groundTruth in falseList:
        falseUniqueWords, falseCount = addOrIncrement(word, falseUniqueWords, falseCount)
      else:
        # We cannot trust the ground truth, figure this out later
        pass


  ## Second loop will determine target words
  #   Criteria for a word to be considered a target word
  #   1. The word must occur more in true statements than in false statements
  #   2. The word must occur two or more times
  #   3. The word length must be lareger than 3 characters

  # Words that appear more in true statements than false statements
  # may should be considered as a possible target word
  for word in trueUniqueWords:

    # Find the index of this word so we can find the number of occurances
    iTrue = trueUniqueWords.index(word)

    # Check if the word occurs more than once and is more than 3 characters
    if trueCount[iTrue] > 1 and len(word) > 3:
  
        if word not in falseUniqueWords:
            # This word has become a targetWord
            targetWords.append(word)
        
        else:
            # This word is both True and False.

            # Grab the indicies so we can compare the number of true vs false occurances
            iFalse = falseUniqueWords.index(word)

            if trueCount[iTrue] > falseCount[iFalse]:
                # The word occures more in true statements
            
                # This word has become a targetWord
                targetWords.append(word)


  # Print first line....
  print('------------------------------------------------------------------------------------------')
  print(" 'TargetWordFound?' / 'GroundTruth' : Classification : Number of target words : Statement ")
  print('------------------------------------------------------------------------------------------')


  ## Third loop will count targetwords
  for lineOfWords in dataList:      #  For each line (list) of words...

    groundTruth = lineOfWords.pop(0)  # The first word of each line represents "Ground Truth"
    twLineCount = 0                   # Count the number of target words in each line

    linesOfData += 1                  # Count the total number of lines of text

    for word in lineOfWords:       # For each word (in this line of text)...

      if word in targetWords:
        # A target word exists in this line, lets count it
        twLineCount += 1

    ### Lets do some classification...
    if twLineCount > 0 and groundTruth in trueList:
      print( "+/+: TP :",twLineCount,': ', end='')
      tpCount += 1
    elif twLineCount > 0 and groundTruth in falseList:
      print( "+/-: FP :",twLineCount,': ', end='')
      fpCount += 1
    elif twLineCount == 0 and groundTruth in trueList:
      print( "-/+: FN : 0 : ", end='')
      fnCount += 1
    elif twLineCount == 0 and groundTruth in falseList:
      print( "-/-: TN : 0 : ", end='')
      tnCount += 1
    else:
      print('?: ', end='')

    # Print out the line of words
    for word in lineOfWords:
      print(word, end=' ')

    # Print a new line for formatting
    print('')


  # All words processed, display summary
  printDetails(targetWords, linesOfData, tpCount, tnCount, fpCount, fnCount)


# Enable this code to be used as a module
if __name__ == "__main__":
  main()

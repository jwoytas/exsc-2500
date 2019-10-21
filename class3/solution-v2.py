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


# This method will read one line from a file and return the words as a list
# It also call normalize_data to remove punctuation, duplicates and convert to lower case
#   Accepts: string filename
#   Returns: list
def readTargetWords(filename):

  twList = []  # A list of target words to be returned

  fo     = safe_open(filename)  # Open the file and catch any errors
  twLine = safe_input(fo)       # Read from the file and catch any errors
  fo.close()                    # Data has been read, close the file

  twList = twLine.split()           # Save all data to the return list
  twList = normalize_data(twList)   # Remove punctuation, duplicates and convert to lowercase

  return twList                     # Return the list of target words


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
def printDetails(targetWords, uniqueWords, uniqueWordCount):
  print('------------------------------------------------------------')
  print('The target words are: ', targetWords)
  print('------------------------------------------------------------')
  print('The first 5 unique words are: ', uniqueWords[0:5])
  print('The number of unique words found: %d'  % len(uniqueWords))
  print('The first 5 unique words counts are: ', uniqueWordCount[0:5])
  print('------------------------------------------------------------')


#####################################
### Program execution begins here ###

def main():
  # Initialize variables
  twFileName = 'target.words.txt'         # Target Words file
  dataFileName = 'weather.txt'            # Data Words file

  uniqueWords = []      # Store all unique Words
  uniqueWordCount = []  # Store the number of times this unique word was found

  # Safely read and normalize target words
  twList = readTargetWords(twFileName)

  # The data List will contain lists for each line of the file. Those lists will contain words
  dataList = readDataWords(dataFileName)

  ## Main analysis loop
  for list in dataList:     #  For each line (list) of words...

    twLineCount = 0         # Count the number of target words in each line

    for word in list:       # For each word (in this line of text)...

      if word in twList:
        # A target word exists in this line, lets count it
        twLineCount = twLineCount + 1

      if word not in uniqueWords:
        # This word has not been seen before, lets remember it and count it
        uniqueWords.append(word)            # Found a unique word
        uniqueWordCount.append(1)           # Count starts at one
      else:
        # This word has been seen before, lets increment its count
        i = uniqueWords.index(word)         # The word is not unique
        uniqueWordCount[i] =  uniqueWordCount[i] + 1  # Increment the word counter

    # If we found a targetWord, lets classify with a '+' or '-'
    # Enchancement: also display the number of (unique) target words found
    if twLineCount > 0:
      print('+', twLineCount, ': ', end='')
    else:
      print('- 0 : ', end='')

    # Print out the line of (unique) words
    for word in list:
      print(word, end=' ')

    # Print a new line for formatting
    print('')

  # All words processed, display summary
  printDetails(twList, uniqueWords, uniqueWordCount )


# Enable this code to be used as a module
if __name__ == "__main__":
  main()

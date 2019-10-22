# This version is 'working', the next version will be clean

# This program reads text input and counts the number of "Target" words.
# It also counts the number of occurances of each unique word
import sys
import string


def safe_open(filename):
  try:
    fo = open(filename, "r")
    return(fo)
  except:
    print("File open failed: %s" % (filename))
    sys.exit(-1)

def safe_input(fo):
  try:
    lineOfWords = fo.readline().strip()
    if lineOfWords == "":
      return ("")
    else:
      return (lineOfWords)
  except:
    return("")

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

# Read all the target words from the target filename
# Args:  filename
# Returns:  a list of target words
def readTargetWords(filename):

  twList = []  # A list of target words to be returned

  fo     = safe_open(filename)  # Open the file and catch any io errors
  twLine = safe_input(fo)       # Read from the file and catch any errors
  fo.close()                # Data has been read, close the file

  twList = twLine.split()     # Save all data to the return list
  twList = normalize_data(twList)  # Remove punctuation, duplicates and convert to lowercase

  return twList                    # Return the list of target words


# Read all the input and return a list of lists containing each line
def readDataWords(filename):

  wList = []          # A list of lists of all the data words
  curList = []        # Current list for each line of text

  fo = safe_open(filename)  # Open the file and catch any io errors

  while True:

    lineOfWords = safe_input(fo)   # Read from the file and catch any errors

    if lineOfWords == "":          # End of data or error exception, break
        break

    curList = lineOfWords.split()
    curList = normalize_data(curList)  # Remove punctuation, duplicates and convert to lowercase

    # Add the current list of words to the complete list
    wList.append(curList)

  fo.close()                # All data has been read, close the file
  return wList


# Display the number of target words
#         the number of unique words
#     and the first 5 unique words
def printDetails(targetWords, uniqueWords, uniqueWordCount):
  print('---------------------------------')
  print('The target words are: ', targetWords)
  print('---------------------------------')
  print('The first 5 unique words are: ', uniqueWords[0:5])
  print('The number of unique words found: %d'  % len(uniqueWords))
  print('The first 5 unique words counts are: ', uniqueWordCount[0:5])
  print('---------------------------------')


def main():
  # Initialize variables
  twFileName = 'target.words.txt'         # Target Words file
  dataFileName = 'weather.txt'            # Data Words file

  twLineCount = 0       # Count the number of target words in each line
  uniqueWords = []      # Store all unique Words
  uniqueWordCount = []  # Store the number of times this unique word was found

  # Safely read and normalize target words
  twList = readTargetWords(twFileName)

  # The data List will contain lists for each line of the file. Those lists will contain words
  dataList = readDataWords(dataFileName)  # Safely read and normalize data words

  #  Debugging
  # print(twList)
  # print(dataList)

  #  For each line (list) of words...
  for list in dataList:

    # For each targetWord (in each line)...
    for word in list:

      if word in twList:
        # A target word exists in this line, lets count it
        twLineCount = twLineCount + 1

      if word not in uniqueWords:
        uniqueWords.append(word)            # Found a unique word
        uniqueWordCount.append(1)           # Count starts at one
      else:
        i = uniqueWords.index(word)         # The word is not unique
        uniqueWordCount[i] =  uniqueWordCount[i] + 1  # Increment the word counter

    # Are there any targetWords, if so classify with a '+' or '-'
    if twLineCount > 0:
      print('+', twLineCount, ': ', end='')
    else:
      print('- 0 : ', end='')

    # Print out the line of (unique) words
    for word in list:
      print(word, end=' ')

    # Print a new line for formatting
    print('')

    # Reset our target count for each line
    twLineCount = 0

  # All words processed, display summary
  printDetails(twList, uniqueWords, uniqueWordCount )

# Enable this code to be used as a module
if __name__ == "__main__":
  main()

# This python program reads input from files target.words.txt, weather.txt
# The program will search for any target word in the data (weather.txt)
# and will classify the line of data accordingly
#
# In addition, the program will also:
#   - Handle properly an end-of-file (EOF) for files
#   – Input files can have multiple words on each line
#   – Count the number of unique words in the input
#   – Use user-defined functions, and main()
#   –NEW: Classify weather.txtlines using target words.
#
# In addition, the program will also:
#   - strip and punctuation and convert all target and data words to lowercase
#

import string

# Read all the target words from the target filename
def readTargetWords(filename):
  twFile = open(filename, 'r')
  twList = []

  try:
    lineOfWords = twFile.readline().strip()
    twList = lineOfWords.split()
    twFile.close()
    return twList

  except IOError:
    print("File open failed: %s" (filename))
    sys.exit(-1)


# Read all the input and return a list of words
def readWords(filename):
  wFile = open(filename, 'r')
  listOfWords = []

  while True:
    try:
      lineOfWords = wFile.readline().strip()

      if lineOfWords == '':
        wFile.close()
        return listOfWords

    except IOError:
      print ("Could not read data file")
      sys.exit(-1)

    #Add current line of words to the complete list of words from all lines of input
    listOfWords.extend(lineOfWords.split())


# Remove punctuaction and convert to lowercase
def normalizeWord(word):
    # Strip punctuation and case
    # - credit: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    word = word.translate(str.maketrans('', '', string.punctuation))
    return word.lower()


# Display the number of target words
#         the number of unique words
#     and the first 5 unique words
def printDetails(targetWords, targetCount, uniqueWords, uniqueWordCount):
  print('---------------------------------')
  print('The target words are: ', targetWords)
  print('Number of target words found: ' + str(targetCount))
  print('---------------------------------')
  print('The first 5 unique words are: ', uniqueWords[0:5])
  print('The number of unique words found: %d'  % len(uniqueWords))
  print('The first 5 unique words counts are: ', uniqueWordCount[0:5])
  print('---------------------------------')


def main():
  # Initialize variables
  targetCount = 0
  uniqueWords = []
  uniqueWordCount = []                    # The number of times the unique word appears

  targetWords = readTargetWords('target.words.txt')
  for word in readWords('input.5'):                # For each word... (read input)

    word = normalizeWord(word)            # Remove punctuation and case

    if word in targetWords:
      targetCount = targetCount + 1       # Found a target word

    if word not in uniqueWords:
      uniqueWords.append(word)            # Found a unique word
      uniqueWordCount.append(1)           # Count starts at one
    else:
      i = uniqueWords.index(word)         # The word is not unique
      uniqueWordCount[i] =  uniqueWordCount[i] + 1  # Increment the word counter

  # All words processed, display summary
  printDetails(targetWords, targetCount, uniqueWords, uniqueWordCount)

# Enable this code to be used as a module
if __name__ == "__main__":
  main()

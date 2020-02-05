import string
import safe_files as sf

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
#   Accepts: fileobject
#   Returns: list of (list of strings)
def readDataWords(fo):

  wList = []          # A list of lists of all the data words
  curList = []        # Current list for each line of text

  while True:

    lineOfWords = sf.safe_input(fo)   # Read from the file and catch any errors

    if lineOfWords == "":          # End of data or error exception, break
      break

    curList = lineOfWords.split()      # Split the line string and save as a list
    curList = normalize_data(curList)  # Remove punctuation, duplicates and convert to lowercase

    wList.append(curList)   # Add the current list of words to the whole file list

  return wList
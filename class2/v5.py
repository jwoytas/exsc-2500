# This program reads text input and counts the number of "Target" words.
# It also counts the number of occurances of each unique word

import string


# Read all the input and return a list of words
def readWords(firstLine=False):
  targetWords = []
  listOfWords = []
  while True:
    try:
      lineOfWords = input()
    except EOFError:
      return listOfWords

# NEW
    if firstLine:
      return lineOfWords.split()

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
  print('The number of unique words found: %d'  % len(uniqueWords))
  print('The first 5 unique words are: ', uniqueWords[0:5])
  print('The first 5 unique words counts are: ', uniqueWordCount[0:5])
  print('---------------------------------')


def main():
  # Initialize variables
  targetCount = 0
  uniqueWords = []
  uniqueWordCount = []                    # The number of times the unique word appears

  targetWords = readWords(True)           # Firstline is True this time only

  for word in readWords():                # For each word... (read input)

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

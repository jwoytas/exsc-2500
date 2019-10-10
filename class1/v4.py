# This program reads text input and counts the number of "Target" words.
# It also counts the number of occurances of each unique word

import string


# Read all the input and return a list of words
def readWords():
  listOfWords = []
  while True:
    try:
      lineOfWords = input()
    except EOFError:
      return listOfWords

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
def printDetails(targetCount, uniqueWords, uniqueWordCount):
  print('Number of target words: ' + str(targetCount))
  print('Number of unique words: %d'  % len(uniqueWords))
  print('The first 5 unique words are: ', uniqueWords[0:5])
  print('The first 5 unique words counts are: ', uniqueWordCount[0:5])



def main():
  # Initialize variables
  targetCount = 0
  targetWords = ["the","data","learn", "python"]
  uniqueWords = []
  uniqueWordCount = []                    # The number of times the unique word appears

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
  printDetails(targetCount, uniqueWords, uniqueWordCount)

# Enable this code to be used as a module
if __name__ == "__main__":
  main()

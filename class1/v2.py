# This program reads text input and counts the number of "Target" words
# and the number of unique words


# Read all the input and return a list of words
def readWords():
  listOfWords = []
  while True:
    try:
      lineOfWords = input()
    except EOFError:
      return listOfWords
    listOfWords.extend(lineOfWords.split())    

# Display the number of target words
#         the number of unique words
#     and the first 5 unique words
def printDetails(targetCount, uniqueWords):
  print('Number of target words: ' + str(targetCount))
  print('Number of unique words: %d'  % len(uniqueWords))
  print('The first 5 unique words are: ', uniqueWords[0:5])


def main():

  # Initialize variables
  targetCount = 0
  targetWords = ["the","The","data","Data","learn", "python", "Python"]
  uniqueWords = []

  for word in readWords():                # For each word do this

    if word in targetWords:
      targetCount = targetCount + 1       # Found a target word

    if word not in uniqueWords:
      uniqueWords.append(word)            # Found a unique word

  printDetails(targetCount, uniqueWords)  # Print summary

main()

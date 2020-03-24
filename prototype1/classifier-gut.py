# This program reads text input and counts the number of "Target" words.
# It also counts the number of occurances of each unique word

import os, sys, logging
import my_log as log
import safe_files as sf
import read_data as rd

# Initialize Logging and set log level
log.start()


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



logging.debug('Start of program')
### Program execution starts here
def main():

  # Initialize variables
  dataFileName   = 'movie_review.txt'
  outputFileName = 'data.md'

  # Open the input data
  dataFile   = sf.safe_open(dataFileName, 'r')    # Open the data file for reading
  
  # inputList is a List of lists.  
  #   Outer list for each line of the file, 
  #   Inner lists hold each word as a string
  inputList = rd.readDataWords(dataFile)

  dataFile.close()



 # Initially we will keep track unique words for 'true' and 'false' ground thruths
  trueUniqueWords = []
  trueCount = []
  falseUniqueWords = []
  falseCount = []

  ## First loop will look count unqiue words for both true and false statements
  for lineOfWords in inputList:      #  For each line (list) of words...

    # The first word of each line represents "Ground Truth"
    groundTruth = lineOfWords[0].lower()[0]

    for word in lineOfWords[1:]:    # For each word (except the first word)...

      # Track unique words and number of occurances in two categories, (true or false)
      if groundTruth == 't':
        trueUniqueWords, trueCount = addOrIncrement(word, trueUniqueWords, trueCount)
      elif groundTruth == 'f':
        falseUniqueWords, falseCount = addOrIncrement(word, falseUniqueWords, falseCount)
      else:
        # We cannot trust the ground truth, figure this out later
        pass


  outputFile = sf.safe_open(outputFileName, 'w')  # Open the output file for writting
  outputFile.close()
  
  logging.debug('End of program')

# Enable this code to be used as a module
if __name__ == "__main__":
  main()

### EXSC-2500 

**University of Alberta - Faculty of Extension**

#### Python Programming and Machine Learning

This repository is to track learning and exercises on the topic of python programming and machine learning.


#####  Class 1 - Introduction to python programming
-  Excercises include writting a python program to:
  - Accept input from the command line and a text file
  - Count 'target words'
  - Count 'unique words'

```python
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
```


#####  Class 2 - Expanding python programming
*  Iteritive software development
*  Using a debugger, breakpoints and inspecting variables
*  Variable scope and User-defined functions
*  Additionial python parsing
```python
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
```


#####  Class 3 - Introduction to Machine Learning
-  Supervised ML and classification
-  Training data
-  Performance and accuaracy metrics 
  - Precision
  - Recall 
  - Ground Truth
- Challenge assignment:
  - Calculate Precision and Recall on a test data file without being given any target words (create your own target words from the data)
```python
    wordsfo.close()
    print( "The number of lines/training instances ", linesOfData)
    print('TP:   %3d  TN:  %3d' % (tpCount, tnCount))
    print('FP:   %3d  FN:  %3d' % (fpCount, fnCount))

    precision = (1.0*tpCount) / (tpCount+fpCount)
    recall =  (1.0*tpCount) / (tpCount+fnCount)
    print('Precision: %5f Recall: %5f' % (precision, recall))
```

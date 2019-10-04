# Count words 'the' and 'The' from input
count = 0
targetWords = ["the","The","data","Data","learn"]
uniqueWords = []

while True:

  try:
    lineOfWords = input()
  except EOFError:
    break

  words = lineOfWords.split()
  for w in words:

    if w in targetWords:
      count = count + 1     # Found one of the two words

    if w not in uniqueWords:
      uniqueWords.append(w)

  print('Count: ' + str(count))

print('Unique Words: ' + str(len(uniqueWords)))
print('Unique Words: %d'  % (len(uniqueWords)), uniqueWords[0:5])

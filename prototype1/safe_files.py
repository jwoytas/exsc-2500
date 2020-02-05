import sys

# This method will attempt to open the file
#   Accepts: string filename, mode (R-Read, A-Append, W-Write)
#   Returns: fileobject
#   Handles exceptions by quiting the program
def safe_open(filename, mode):
  try:
    fo = open(filename, mode)
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
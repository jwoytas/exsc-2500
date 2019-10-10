
def safe_open(filename):
  try:
    fo = open(filename, "r")
    return(fo)
  except:
    print("File open failed: %s" (filename))
    sys.exit(-1)

def safe_input(fo):
  try:
    lineOfWords = fo.readline().strip()
    if lineOfWords == "":
      return ("", False)
    else:
      return (lineOfWords, True)
  except:
    return("",False)

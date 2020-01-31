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


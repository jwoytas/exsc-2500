# This program reads text input and counts the number of "Target" words.
# It also counts the number of occurances of each unique word

import os, sys, logging
from pathlib import Path

import safe_files as sf

# Initialize Logging
logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

"""
Set your logging level here 
DEBUG, INFO, WARNING, ERROR, CRITICAL
"""
logging.disable(logging.DEBUG)


logging.debug('Start of program')
### Program execution starts here
def main():

  # Initialize variables
  dataFileName   = 'movie_review.txt'
  outputFileName = 'data.md'

  logging.warning('Start of File Opening')

  print(Path.cwd())
  df = sf.safe_open(dataFileName, 'r')    # Open the data file for reading
  of = sf.safe_open(outputFileName, 'w')  # Open the output file for writting

  df.close()
  of.close()
  
  logging.critical('End of program')

# Enable this code to be used as a module
if __name__ == "__main__":
  main()

import logging

def start():
    # Initialize Logging
    logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


    """
    Set your logging level here 
    DEBUG, INFO, WARNING, ERROR, CRITICAL
    """

    # Disables Debug messages
    logging.disable(logging.DEBUG)
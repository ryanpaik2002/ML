import csv 
import json
import os


""" 
This script will convert a csv file to a json file.
The csv file must be in the ingest folder.
The json file will be created in the data folder.
Very limited script currently that will not do any data validation checks

"""


DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
CSV_PATH= os.path.join(os.path.dirname(__file__), 'ingest')


# FOR AUTO INGEST OF CSV FILES IN INGEST FOLDER            
# if CSV_PATH is not None:
#     csv_files = os.listdir(CSV_PATH)
# else: 
    # throw error with statement, no csv files fouund
# TODO:
# write a function that will do a dynamic search of csv comparison with json file anem
# need a check for json file name and csv file name match




# TODO:
# write a function tha that will name of the json file based on the csv file name

csv_filename = os.path.join(os.path.dirname(__file__), 'ingest', 'filename.csv')

json_filename = os.path.join(os.path.dirname(__file__), 'data', 'jsonfilenam.json')
# make a log file in the log folder including the date into the name of the file

csv_data = []

with open(csv_filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    word_count = 0
    for row in csv_reader:
        csv_data.append(row)
        word_count += 1
        
        
with open(json_filename, mode="w") as json_file:
    json.dump(csv_data, json_file, indent=4)


import os
from datetime  import datetime
import logging


log_dir = 'logs'

os.makedirs(log_dir, exist_ok=True) 

# Get the current timestamp
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Create the log file with the desired filename
log_file = os.path.join(log_dir, f'ingest_log_{current_time}.log')

logging.basicConfig(filename=log_file, level=logging.INFO) # format='%(asctime)s - %(levelname)s - %(message)s'
logging.info('This message should go to the log file')

logging.info(f"CSV file '{csv_filename}' has been converted to JSON file '{json_filename}'.")
logging.info(f"Word count: {word_count}")





# Configure the logging to write to the log file
# logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log some messages




#TODO:
# MAKE FOR LOOP TO ITERATE OVER CSV FILES IN INGEST FOLDER


# need to rewrite to test update date on json with csv file
# MAKE OPERATION RULE: DO NOTE UPDATE JSON FILES< make NEW FILES AND DISTINCTIONS
# AFTER INGEST OF CSV FILES MOVE CSV FILES TO ARCHIVE

#TODO:
# WHEN LEVELS ARE PICKED, MATCH LEVEL STRING WITH FILE NAME STRING WITHOUT EXTENSION


# TODO: 
# write a log file for each ingest 
# LEVEL, TOTAL SECTIONS, DATE and TIME INGESTED

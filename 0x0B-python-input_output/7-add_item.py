#!/usr/bin/python3

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Get command-line arguments (excluding the script name)
arguments = sys.argv[1:]

# Convert the command-line arguments into a Python list
new_list = list(arguments)

# Specify the filename for the JSON file
filename = "add_item.json"

try:
    # Attempt to load existing data from the JSON file
    existing_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    existing_list = []

# Merge the existing data with the command-line arguments
new_list.extend(existing_list)

# Save the combined data to the JSON file
save_to_json_file(new_list, filename)

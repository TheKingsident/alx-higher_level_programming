#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
new_list = list(arguments)
filename = "add_item.json"

if load_from_json_file(filename):
    existing_list = load_from_json_file(filename)
    new_list.append(existing_list)
    
save_to_json_file(new_list, filename)

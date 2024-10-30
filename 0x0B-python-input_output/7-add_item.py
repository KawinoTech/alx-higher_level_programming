#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
A script that adds all arguments to a Python list, and then save them to a file
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
"""

import sys
file_name = './add_item.json'
with open(file_name, 'a+', encoding="UTF-8") as f:
    list1 = [i for i in load_from_json_file(file_name) if i]
    list2 = [i for i in sys.argv[1:] if i]
    save_to_json_file((list1 + list2), file_name)

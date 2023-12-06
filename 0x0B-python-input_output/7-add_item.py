#!/usr/bin/python3
"""Now we are going to add items in a json file and read them."""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = list(sys.argv[1:])
save_to_json_file(args, "add_item.json")
load_from_json_file("add_item.json")

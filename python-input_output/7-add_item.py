#!/usr/bin/python3
# script that adds all arguments to a Python list,
# and then save them to the file//
"""
    script that adds all arguments to a Python list,
    and save them to a file
"""

import sys

if _name_ == "_main_":
    save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        _import_('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
#!/usr/bin/python3
"""This is the file"""


import json


def save_to_json_file(my_obj, filename):
    """ This is a function that writes object to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))

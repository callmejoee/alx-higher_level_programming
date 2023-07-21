#!/usr/bin/python3
import json
"""This is the file"""

def load_from_json_file(filename):
    """ This is a function that reads objects FROM a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return (json.loads(file.readline()))
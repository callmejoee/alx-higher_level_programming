#!/usr/bin/python3
"""This is the file"""


import json


def load_from_json_file(filename):
    """ This is a function that reads objects FROM a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return (json.loads(file.readline()))

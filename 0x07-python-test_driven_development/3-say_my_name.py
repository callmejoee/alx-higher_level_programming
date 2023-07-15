#!/usr/bin/python3
""" This is a module """


def say_my_name(first_name, last_name=""):
    """
    Function to print an introduction

    :param first_name: first name
    :param last_name: second or last name
    :return: str that introduces the person

    :raises TypeError: if the first name or last name aren't strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

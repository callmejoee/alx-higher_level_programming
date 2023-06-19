#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_set = set()
    for element in set_1:
        for element2 in set_2:
            if element != element2:
                my_set.add(element)
                my_set.add(element2)
    return my_set

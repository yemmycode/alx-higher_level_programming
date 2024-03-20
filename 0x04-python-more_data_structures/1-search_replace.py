#!/usr/bin/python3

def search_replace(my_list, search, replace):

    result_list = []
    for item in my_list:
        if item == search:
            result_list.append(replace)
        else:
            result_list.append(item)
    return result_list

#!/usr/bin/python3
def search_replace(my_list, search, replace):
new_list = []    
    for element in my_list:
        if my_list == search:
            new_list = my_list.append(replace)
        else:
            new_list = my_list.append(element)
        return my_list(element)


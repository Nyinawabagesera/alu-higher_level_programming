def max_integer(my_list=[]):
    if not my_list:
        return None
    max_integer = my_list[0]
    for item in my_list:
        if item > max_integer:
            max_integer = item

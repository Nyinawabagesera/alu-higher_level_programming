#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        if count == x:
                break
            print(my_list[count], end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
~                                                                                                                                                    
~                    

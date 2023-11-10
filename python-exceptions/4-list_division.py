#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            # Attempt to perform the division
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            # Handle wrong type
            print("wrong type")
            result = 0
        except IndexError:
            # Handle index out of range
            print("out of range")
            result = 0
        finally:
            # Append the result to the new_list
            new_list.append(result)
            # Print a message that will always be executed
            print("This will always be executed")
    return new_list

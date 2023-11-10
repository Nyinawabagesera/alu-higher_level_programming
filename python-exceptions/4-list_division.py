#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
                print("Can't divide by Zero")
                return 0
        except TypeError:
                print("wrong type")
                return 0
        except IndexError:
                print("out of range")
                return 0
        finally:
                print("This will always be executed")
    return new_list


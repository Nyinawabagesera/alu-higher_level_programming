#!/usr/bin/python3
def raise_exception_msg(message=""):

try:
  raise_exception_msg(" is fun")
except NameError as ne:
    print(ne)

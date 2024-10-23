#!/usr/bin/python3

def safe_print_integer(value):
    try:
        i = 1 + value
        print(value)
        return True
    except Exception as e:
        return False

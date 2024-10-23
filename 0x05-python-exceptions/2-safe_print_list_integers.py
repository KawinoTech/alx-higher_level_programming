#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for y in range(0, x):
        try:
            if not isinstance(my_list[y], int):
                continue
            print(my_list[y], end="")
            i += 1
        except Exception:
            raise IndexError
    print('\n', end="")
    return i

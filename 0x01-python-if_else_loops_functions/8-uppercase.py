#!/usr/bin/python
def uppercase(str):
    for c in str:
        if(c >= 'a' and c <= 'z'):
           c = chr(ord(c) - 32)
        print("%c" % c, end="")
    print("")

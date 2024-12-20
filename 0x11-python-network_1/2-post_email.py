#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse
    value = {'email' : argv[2] }
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
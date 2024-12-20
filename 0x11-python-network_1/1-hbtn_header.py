#!/usr/bin/python3
"""
Module: Fetch Custom HTTP Header

Description:
This module fetches and displays the value of the
`X-Request-Id` header from the HTTP response
of a specified URL. It uses `urllib.request.urlopen` to send the request.

Usage:
- Run the script from the command line, passing the URL as the first argument:
  $ ./script_name.py <URL>
- Outputs the value of the `X-Request-Id` header.

Dependencies:
- sys: Used to read the URL argument from the command line.
- urllib.request: Used to make the HTTP request.
"""

if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen

    with urlopen(argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))

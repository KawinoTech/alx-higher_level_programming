#!/usr/bin/python3
"""
Module: Fetch Custom HTTP Header

Description:
This module fetches and displays the value of the
`X-Request-Id` header from the HTTP response
of a specified URL. It uses `urllib.request.urlopen` to send the request.
"""

import urllib.request


if __name__ == "__main__":
    import sys
    import urllib

    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))

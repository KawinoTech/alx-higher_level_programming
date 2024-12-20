#!/usr/bin/python3
"""
Module: Fetch URL Content and Handle Errors

Description:
This module fetches the content from a specified URL,
decodes the response body into UTF-8, 
and handles URL-related errors. It prints the error code if the URL is invalid.
"""
if __name__ == "__main__":
    import urllib
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            resp_data = resp.read()
            body_string = resp_data.decode('utf-8')
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")

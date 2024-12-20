#!/usr/bin/python3
"""
Module: Fetch URL Content and Handle Errors

Description:
This module fetches the content from a specified URL, decodes the response body into UTF-8, 
and handles URL-related errors. It prints the error code if the URL is invalid.

Usage:
- Run the script, passing the URL as the first argument:
  $ ./script_name.py <URL>
- If the request is successful, the script decodes the content from the URL.
- If an error occurs (e.g., invalid URL), it prints the error code.

Dependencies:
- sys: Used to fetch the URL from command-line arguments.
- urllib: Used to make the HTTP request and handle errors.

Example:
$ ./script_name.py https://example.com
Output:
Decoded content from the page (if valid).

Error Handling:
If the URL is invalid, the script catches the error and prints an error message in the following format:
Error code: <error_code>

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

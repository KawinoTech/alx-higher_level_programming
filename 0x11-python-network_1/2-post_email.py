#!/usr/bin/python3
"""
Module: Send POST Request with Email

Description:
This module sends a POST request to a specified URL 
with an email address in the payload.
The email is hardcoded as `hr@holbertonschool.com`, and 
the response is printed after being decoded.

Usage:
- Run the script, which sends a POST request to argv[0].
- The email address `hr@holbertonschool.com` is sent as a form-encoded payload.

Dependencies:
- sys: Used to read command-line arguments (if needed in another context).
- urllib.request: Used to send the HTTP POST request.
- urllib.parse: Used to encode the payload data.

Example:
$ ./script_name.py
Output:
The response content from the server is printed, 
typically in UTF-8 encoded format.

Notes:
- The script sends data to a local server at argv[0].
- Adjust the email address or URL as necessary for different use cases.

"""
if __name__ == "__main__":
    import sys
    import urllib

    value = {'email': sys.argv[1]}
    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(sys.argv[0], data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))

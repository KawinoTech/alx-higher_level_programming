#!/usr/bin/python3
"""
Module: Fetch Web Status

Description:
This module fetches data from a specified URL using `urllib.request.urlopen`,
processes the HTTP response, and displays the response type, raw content,
and UTF-8 decoded content in a formatted output.
"""

if __name__ == "__main__":
    import urllib

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        resp_data = resp.read()
        body_string = resp_data.decode('utf-8')
        body_type = type(resp_data)
        print(
            "Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}\n"
            "\t- utf8 content: {}".format(body_type, resp_data, body_string)
        )

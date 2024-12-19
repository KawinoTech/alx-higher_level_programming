#!/bin/bash
#DELETE request to the URL passed as the first argument and displays the body of the response
curl --silent -I -X OPTIONS $1 | grep Allow | cut -d ": " -f 2

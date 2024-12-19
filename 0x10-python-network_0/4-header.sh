#!/bin/bash
#GET request to the URL, and displays the body of the response
curl --silent -H "X-School-User-Id: 98" -X GET $1

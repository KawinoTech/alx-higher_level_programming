#!/bin/bash
#GET request to the URL, and displays the body of the response only 200 status code
curl -L -X GET  --silent $1

#!/bin/bash
#Fetches the headers of the URL provided filters the Content-Length(value in bytes)
curl --silent -I $1 | grep Content-Length | cut -d " " -f 2


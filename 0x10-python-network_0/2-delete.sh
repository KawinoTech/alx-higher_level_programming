#!/bin/bash
#DELETE request to the URL passed as the first argument and displays the body of the response
curl --silent -X DELETE $1

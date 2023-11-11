#!/bin/bash 
# send request to URL passed as an argument and display only the status of code of the response
curl -s -L -X HEAD -w "%{http_code}" "$1"

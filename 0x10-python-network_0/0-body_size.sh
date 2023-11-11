#!/bin/bash
#send request to URL to display content-length
curl -s "$1" | wc -c

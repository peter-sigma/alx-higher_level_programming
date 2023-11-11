#!/bin/bash
# listing http methods in curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

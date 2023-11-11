#!/bin/bash
# sending POST request and displaying the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"

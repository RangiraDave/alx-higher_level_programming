#!/bin/bash
# Script to display all methods allowed by the server
curl -sI "$1" | grep -i "Allow" | awk -F ': ' '{print substr($0, index($0, $2))}'

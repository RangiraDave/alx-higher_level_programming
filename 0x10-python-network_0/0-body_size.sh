#!/bin/bash
# Script to read URL from the args
curl -sI "$1" | grep -i "Allow" | awk -F ': ' '{printf substr($0, index($0,$2))}'

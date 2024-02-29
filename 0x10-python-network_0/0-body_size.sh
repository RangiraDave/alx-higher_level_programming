#!/bin/bash
# Script to read URL from the args
# Send a request to it
# And print its body size.

if [ "$#" -ne 1 ]; then
	echo "Usage: ./0-body_size.sh <URL/IP Adress>"
	exit 1
fi

url="$1"
size=$(curl -sI "$url" | grep -i 'content-length' | awk '{print $2}')

echo "$size"

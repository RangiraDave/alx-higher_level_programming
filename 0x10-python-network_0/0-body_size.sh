#!/bin/bash
# Script to read URL from the args
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'

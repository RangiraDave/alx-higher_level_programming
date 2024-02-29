#!/bin/bash
# Script to implement delete
curl -sXL "DELETE" "$1" | awk 'NR==1,/^\r$/ {if($2 == 200); {printf $0}}'

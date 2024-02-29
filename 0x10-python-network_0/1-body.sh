#!/bin/bash
# Script to display a body of the GET response (/^\r$/ identifies empty line btn header and body)
curl -siX "GET" "$1" | grep -i "200" | awk '/^\r$/ {body=1; next} {if(body) print}'

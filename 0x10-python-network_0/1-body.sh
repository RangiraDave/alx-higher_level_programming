#!/bin/bash
# Script to display a body of the GET response (/^\r$/ identifies empty line btn header and body)
curl -s "$1" | awk 'NR==1,/^\r$/ {if($2 == 200) {body=1}} {if(body) print}'

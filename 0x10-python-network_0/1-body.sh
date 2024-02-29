#!/bin/bash
# Script to display a body of the GET response (/^\r$/ identifies empty line btn header and body)
curl -siX "GET" "$1" | awk 'NK==1,/^\r$/ {if($1 == 200) {body=1}} {if(body) print}'

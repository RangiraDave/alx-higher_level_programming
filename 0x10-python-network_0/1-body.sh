#!/bin/bash
# Script to display a body of the GET response (/^\r$/ identifies empty line btn header and body)
curl -sL "$1" | awk 'NR==1,/^\r$/ {print "Line:", $0; if($2 == 200) {body=1}} {if(body) print}'

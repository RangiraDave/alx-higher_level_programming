#!/bin/bash
# Script to display body of the GET response (/^\r$/ identifies empty line btn header and body)
curl -sL "$1" | awk 'NR==1,/^\r$/ {printf $0; if($2 == 200)}'

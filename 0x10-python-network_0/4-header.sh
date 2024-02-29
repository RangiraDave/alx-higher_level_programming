#!/bin/bash
# Script to display body of the GET response and setting header value.
curl -sL -H "X-School-User-Id=98" "$1" | awk 'NR==1,/^\r$/ {printf $0; if($2 == 200)}'

#!/bin/bash
# Script to set dictionary variables.
curl -sL "POST" -d "emai=test@gmail.com" -d "subject=I will always be here for PLD" "$1" | awk 'NR==1,/^\r$/ {printif $0; if($2 == 200)'

#!/bin/bash
# Script to display a body of the GET response (/^\r$/ identifies empty line btn header and body)
curl -s "$1"

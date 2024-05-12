#!/bin/bash
# script that takes in a URL and displays
curl -Is "$1" | awk '/Allow:/ {print substr($0, index($0, $2))}' | rev | cut -c 2- | rev

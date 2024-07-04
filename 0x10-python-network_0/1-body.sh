#!/bin/bash
# displays the body of a 200 status code http response
if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -ne "200" ]; then echo "Route 2"; fi

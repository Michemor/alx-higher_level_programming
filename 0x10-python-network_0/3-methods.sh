#!/bin/bash
# displays all HTTP methods the server
curl -sI -X "OPTIONS" "$1" | awk '/Allow/ {print $2, $3, $4}'

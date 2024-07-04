#!/bin/bash
# displays all HTTP methods the server
curl -sI -X "OPTIONS" "$1" | grep -i "Allow" | cut -d " " -f2-

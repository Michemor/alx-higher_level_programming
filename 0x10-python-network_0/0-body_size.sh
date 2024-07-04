#!/bin/bash
# sends a request to that URL and displays the size of the body
echo "$(curl -sI "$1" | awk '/Content-Length/ {print $2}')"

#!/bin/bash
# sends a GET request with a specified header variable
curl -s -H "X-School-User-id: 98" "$1"

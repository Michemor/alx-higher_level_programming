#!/bin/bash
# sends a DELETE request
if ["$(curl -sI -o /dev/null -w "%{http_code}" -X DELETE "$1")" -eq "200" ]; then echo "I'm a DELETE request"; fi

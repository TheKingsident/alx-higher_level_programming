#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -i -s "http://$1" | grep 'Allow:' | cut -d ' ' -f2- | tr -d '\r'

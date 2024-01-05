#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -i -s 0.0.0.0:5000/route_4 | grep 'Allow:' | cut -d ' ' -f2- | tr -d '\r'

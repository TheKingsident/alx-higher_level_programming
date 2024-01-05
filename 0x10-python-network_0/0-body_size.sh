#!/bin/bash
# Displays the size of the body of a HTTP Response
curl -w "%{size_download}\n" -o /dev/null -s "http://$1"

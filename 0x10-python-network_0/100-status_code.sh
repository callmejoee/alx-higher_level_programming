#!/bin/bash
# this is curl
curl -s -o /dev/null -w "%{http_code}" "$1"

#!/bin/bash
# this is a script to get size of response message
curl -s "$1" | wc -c

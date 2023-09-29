#!/bin/bash
# this send the required stuff
curl -sX POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"

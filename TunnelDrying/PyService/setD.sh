#!/bin/sh

cd /home/pi/DryingExp/PyService
python setDate.py "$1 $2 $3 $4 $5 $6 $7 $8 $9 $10"
echo "$1 $2 $3 $4 $5 $6 $7 $8 $9 $10"
#date -s "$1 $2 $3 $4 $5 $6 $7 $8 $9 $10"
echo date


 

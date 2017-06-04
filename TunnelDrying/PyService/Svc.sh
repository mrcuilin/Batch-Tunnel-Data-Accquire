#!/bin/sh
ps -fe | grep python | grep ReadService
if [ $? -ne 0 ]
then
echo "START RUN"
python ReadService.py &
else
echo "ALready RUnning"
fi





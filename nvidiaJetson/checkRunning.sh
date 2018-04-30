#!/bin/bash
SERVICE='love_apparatus.py'
 
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
    echo "$SERVICE service running, everything is fine"
else
    echo "$SERVICE is not running"
    export DISPLAY=:0 && python3 /home/nvidia/Documents/loveapparatus/love_apparatus.py
fi
